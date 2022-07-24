#!/usr/bin/env pytest

import pytest
import wordle_helper

def test_load_words():
    num_words = len(wordle_helper.load_words())
    assert num_words == 15918

full_word_list = wordle_helper.load_words()
empty_set = set()

@pytest.mark.parametrize("guess_list,given_letters,dupe_letters,expected_result", [
    (
        full_word_list,
        ['r', 's', 't', 'l', 'n', 'e', 'a', 'e', 'i', 'o', 'm', 'p', 'y', 'k', 'z', 'x', 'f', 'g', 'd', 'c'],
        {'e'},
        ['beeve', 'behew', 'bevue', 'jubbe', 'queue', 'veuve', 'wehee']
    ),
])

def test_process_misses(guess_list, given_letters, dupe_letters, expected_result):
    result = wordle_helper.process_misses(guess_list, given_letters, dupe_letters)
    assert sorted(result) == expected_result
