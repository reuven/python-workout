from e12_most_repeating_letters import most_repeating_letter_count, most_repeating_word, WORDS
import pytest


@pytest.mark.parametrize('one_word, count', [
    ('banana', 3),
    ('apple', 2),
    ('balloon', 2),
    ('abcabcabca', 4)
])
def test_most_repeating_letter_count(one_word, count):
    assert most_repeating_letter_count(one_word) == count


@pytest.mark.parametrize('list_of_words, one_word', [
    (WORDS, 'elementary'),
    ('hello out there'.split(), 'hello'),
    ('there out hello'.split(), 'there')
])
def test_most_repeating_word(list_of_words, one_word):
    assert most_repeating_word(list_of_words) == one_word
