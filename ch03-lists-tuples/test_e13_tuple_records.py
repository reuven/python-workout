from e13_tuple_records import format_sort_records, PEOPLE


def test_empty():
    assert format_sort_records([]) == []


def test_with_people():
    output = format_sort_records(PEOPLE)
    assert isinstance(output, list)
    assert all(isinstance(x, str) for x in output)

    assert output[0][:10].strip() == 'Putin'
    assert output[0][10:20].strip() == 'Vladimir'
    assert output[0][20:].strip() == '3.63'
