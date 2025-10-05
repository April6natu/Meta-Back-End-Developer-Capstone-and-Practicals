import pytest

def test_example():
    assert 2 + 2 == 4

def test_string():
    assert "hello".upper() == "HELLO"

def test_list():
    assert len([1, 2, 3]) == 3