from datetime import date
from seasons import convert_date
import pytest

def tes_convert_date1():
    assert convert_date("1998-10-09") == date(1998, 10, 9)



def test_convert_date2():
    with pytest.raises(ValueError):
        convert_date("01-01-01")
