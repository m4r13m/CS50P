from plates import is_valid

def test_one():
    assert is_valid("H") == False
    assert is_valid("GOODBYE") == False

def test_two():
    assert is_valid("CS 50") == False
    assert is_valid("PI3.14") == False

def test_three():
    assert is_valid("HELLO") == True
    assert is_valid("66H") == False
    assert is_valid("8AA") == False
    assert is_valid("H777") == False

def test_four():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
