from detector.utils import is_cyrillic


def test_is_cyrillic():
    assert is_cyrillic('Слово 12313')
    assert is_cyrillic('Пример: 2 + 2 == 4')
    assert is_cyrillic('Ёлка.')


def test_is_not_cyrillic():
    assert not is_cyrillic('Word')
    assert not is_cyrillic('Язык программирования Python')
    assert not is_cyrillic('Мой ник - name1234')
