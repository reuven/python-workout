from e11_alphabetize_names import alphabetize_names, PEOPLE


def test_empty():
    assert alphabetize_names([]) == []


def test_with_people():
    assert PEOPLE[0]['last'] == 'Lerner'
    assert PEOPLE[1]['last'] == 'Trump'
    assert PEOPLE[2]['last'] == 'Putin'

    output = alphabetize_names(PEOPLE)
    assert output[0]['last'] == 'Lerner'
    assert output[1]['last'] == 'Putin'
    assert output[2]['last'] == 'Trump'
