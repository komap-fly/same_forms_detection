import string
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

RUSSIAN_LETTERS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
RUSSIAN_LETTERS += RUSSIAN_LETTERS.upper()
RUSSIAN_LETTERS = set(RUSSIAN_LETTERS)


def is_cyrillic(phrase: str) -> bool:
    return all(letter in RUSSIAN_LETTERS for letter in phrase if letter.isalpha())


def number_of_words(phrase: str) -> int:
    words = [i.strip(string.punctuation) for i in phrase.split()]
    return len([word for word in words if any(w.isalpha() for w in word)])


def _gen_error(message):
    return {
        'status': 'error',
        'message': message
    }


def generate_response(phrase: str) -> dict:
    if not is_cyrillic(phrase):
        return _gen_error('В предложении должен присутствовать только русский текст')
    words = [i.strip(string.punctuation) for i in phrase.split()]
    first = ''
    try:
        first = words[0]
    except IndexError:
        pass
    first = first.strip()
    if len(first) == 0:
        return _gen_error('Пустое предложение')
    if first.isdigit():
        return _gen_error('Первое слово является числом')
    forms = set([parse.normal_form for parse in morph.parse(first)])
    forms.add(first.lower())
    for word in words[1:]:
        word_forms = {parse.normal_form for parse in morph.parse(word)}
        word_forms.add(word)
        if len(forms & word_forms) > 0:
            forms |= word_forms
    return {
        'status': 'ok',
        'declined_word': list(sorted(forms)),
        'num_words': number_of_words(phrase)
    }
