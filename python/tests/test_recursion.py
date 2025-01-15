from scripts.recursion import factorial


def test_recursion():
    res = factorial(5)
    assert res == 120


def test_recursion_base_case():
    res = factorial(1)
    assert res == 1
