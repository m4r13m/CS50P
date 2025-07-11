from working import convert
import pytest

def test_one():
    assert convert("7 AM to 9 PM") == "07:00 to 21:00"
    assert convert("9:23 AM to 12 AM") == "09:23 to 00:00"
    assert convert("12:59 AM to 12:21 PM") == "00:59 to 12:21"

def test_two():
    with pytest.raises(ValueError):
        convert("4:60 PM to 4:10 AM")

def test_three():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("09:00 AM - 17:00 PM")
