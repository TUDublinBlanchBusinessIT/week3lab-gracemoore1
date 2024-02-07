#test_perfectNumber.py
import pytest
from perfectNumber import perfectNumber

def test_divisors():
    assert perfectNumber(8128) == True
