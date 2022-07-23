#!/usr/bin/env pytest

import wordle_helper

def test_load_words():
    num_words = len(wordle_helper.load_words())
    assert num_words == 15918

