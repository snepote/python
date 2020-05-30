def inc(x):
    return x + 1


def test_wrong():
    assert inc(3) != 5

def test_correct():
    assert inc(4) == 5
