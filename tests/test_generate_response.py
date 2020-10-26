from detector.utils import generate_response


def test_error_cases():
    assert generate_response('') == {
        'status': 'error',
        'message': 'Пустое предложение'
    }
    assert generate_response('   ,') == {
        "status": 'error',
        'message': 'Пустое предложение'
    }
    assert generate_response('Текст текст word') == {
        'status': 'error',
        'message': 'В предложении должен присутствовать только русский текст'
    }
    assert generate_response('42 , слово') == {
        'status': 'error',
        'message': 'Первое слово является числом'
    }


def test_counts_forms():
    sentence = 'Любая любой любые слово проверка 42'
    assert generate_response(sentence) == {
        'status': 'ok',
        'declined_word': ['люба', 'любая', 'любой', 'любые'],
        'num_words': 5
    }
