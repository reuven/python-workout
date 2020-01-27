from e11_alphabetize_names import alphabetize_names, people


def test_empty():
    assert alphabetize_names([]) == []


def test_with_people():
    assert people[0]['last'] == 'Lerner'
    assert people[1]['last'] == 'Trump'
    assert people[2]['last'] == 'Putin'

    output = alphabetize_names(people)
    assert output[0]['last'] == 'Lerner'
    assert output[1]['last'] == 'Putin'
    assert output[2]['last'] == 'Trump'
