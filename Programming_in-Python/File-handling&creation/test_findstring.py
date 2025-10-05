from curses.ascii import isdigit
import findstring
import pytest

def test_ispresent():
    assert findstring.ispresent("Al")