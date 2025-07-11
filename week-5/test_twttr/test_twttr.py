from twttr import shorten

def test_shorten():
    assert shorten("HELLO, WORLD") == "HLL, WRLD"
    assert shorten("This is CS50") == "Ths s CS50"
    assert shorten("CS50 Python 2025") == "CS50 Pythn 2025"
