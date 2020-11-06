#!/usr/bin/env python3

import pytest
from fizzbuzz import *

# This is the most simple basic test for pytest to ensure we've set things up properly

def check_fizzBuzz(value, expected_response):
    assert expected_response == fizzBuzz(value)

def test_canAssertTrue():
    assert True

def test_fizzBuzz0():
    check_fizzBuzz(0, "0")

def test_fizzBuzz1():
    check_fizzBuzz(1, "1")

def test_fizzBuzz2():
    check_fizzBuzz(2, "2")

def test_fizzBuzz3():
    check_fizzBuzz(3, "Fizz")

def test_fizzBuzz5():
    check_fizzBuzz(5, "Buzz")

def test_fizzBuzz6():
    check_fizzBuzz(6, "Fizz")

def test_fizzBuzz10():
    check_fizzBuzz(10, "Buzz")

def test_fizzBuzz15():
    check_fizzBuzz(15, "FizzBuzz")

def test_fizzBuzz30():
    check_fizzBuzz(30, "FizzBuzz")

def test_fizzBuzzDecimal():
    check_fizzBuzz(30.0, "30.0")

def test_fizzBuzzStr():
    check_fizzBuzz("hello", "hello")

