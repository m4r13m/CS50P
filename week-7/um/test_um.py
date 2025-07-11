from um import count

def test_one():
    assert count("um...") == 1
    assert count("UM") == 1

def test_two():
    assert count("um.. mum..um..") == 2
    assert count("album um mum") == 1


def test_three():
    assert count("UM, thanks yummy") == 1
