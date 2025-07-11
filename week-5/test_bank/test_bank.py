from bank import value

def test_one():
    assert value("Hello, world") == 0
    assert value("HELLOOO") == 0

def test_two():
    assert value("Hey, there") == 20
    assert value("How you doing?") == 20

def test_three():
    assert value("This is CS50") == 100
    assert value("Bonjour") == 100
