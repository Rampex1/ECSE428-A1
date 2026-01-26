import pytest
from cdc import ComplexCalculator


def test_push_pop_real_number():
    """T-PUSH-REAL1: push 5 pop -> 5 + j0"""
    calc = ComplexCalculator()
    calc.push("5")
    result = calc.pop()
    assert result == "5 + j0"
