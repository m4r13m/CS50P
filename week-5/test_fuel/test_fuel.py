from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
    with pytest.raises(ValueError):
        convert("-1/4")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(67) == "67%"
    assert gauge(99) == "F"

