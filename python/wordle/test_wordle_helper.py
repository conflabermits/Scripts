#!/usr/bin/env pytest

# Props to kinjasloth and IRegretzu for the help!

import pytest
import wordle_helper

def test_load_words():
    num_words = len(wordle_helper.load_words())
    assert num_words == 15918

full_word_list = wordle_helper.load_words()
empty_set = set()

@pytest.mark.parametrize("missed_letters,dupe_letters,expected_result", [
    (
        ['r', 's', 't', 'l', 'n', 'e', 'a', 'e', 'i', 'o', 'm', 'p', 'y', 'k', 'z', 'x', 'f', 'g', 'd', 'c'],
        {'e'},
        ['beeve', 'behew', 'bevue', 'jubbe', 'queue', 'veuve', 'wehee']
    ),
    (
        ['r', 's', 't', 'l', 'n', 'e', 'a', 'i', 'o', 'm', 'p', 'y'],
        empty_set,
        ['buchu', 'bucku', 'buddh', 'chubb', 'chuck', 'chuff', 'kudzu', 'whuff']
    ),
])

def test_process_misses(missed_letters, dupe_letters, expected_result):
    result = wordle_helper.process_misses(full_word_list, missed_letters, dupe_letters)
    assert sorted(result) == expected_result

@pytest.mark.parametrize("green_letters,expected_result", [
    (
        ['1r', '2u', '4t'],
        ['runts', 'runty', 'rusts', 'rusty', 'rutty']
    ),
    (
        ['2n', '4k'],
        ['angka', 'ensky', 'snake', 'snaky', 'snoke', 'ungka']
    ),
])

def test_process_greens(green_letters, expected_result):
    result = wordle_helper.process_greens(full_word_list, green_letters)
    assert sorted(result) == expected_result

@pytest.mark.parametrize("yellow_letters,expected_result", [
    (
        ['2z', '1b', '5r'],
        ['zabra', 'zebra']
    ),
    (
        ['1t', '2t', '3b', '5u', '4s'],
        ['abuts', 'bhuts', 'bouts', 'bunts', 'busti', 'busto', 'busts', 'busty', 'butts']
    ),
])

def test_process_yellows(yellow_letters, expected_result):
    result = wordle_helper.process_yellows(full_word_list, yellow_letters)
    assert sorted(result) == expected_result
