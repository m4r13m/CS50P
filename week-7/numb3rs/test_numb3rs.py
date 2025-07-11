from numb3rs import validate

def test_one():
    assert validate("1.0.1.0") == True
    assert validate("255.255.255.255") == True

def test_two():
    assert validate("256.1.1.1") == False
    assert validate("1000") == False
    assert validate("145.123.0.158.241") == False
    assert validate("123.256.256.288") == False
