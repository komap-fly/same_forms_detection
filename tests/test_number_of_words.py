from detector.utils import number_of_words


def test_empty_string_means_zero():
    assert number_of_words('') == 0


def test_without_punctuation():
    assert number_of_words('Слово 1234') == 1
    assert number_of_words('Кто-то прошёл по улице.') == 4
    assert number_of_words('nickname1234 0') == 1


def test_with_punctuation():
    assert number_of_words('Что? Где? Когда?') == 3
