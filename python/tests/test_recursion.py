from scripts.recursion import factorial, sum_arr


def test_factorial():
    res = factorial(5)
    assert res == 120


def test_factorial_base_case():
    res = factorial(1)
    assert res == 1


def test_sum_arr():
    arr = [2, 3, 5, 7, 11]
    res = sum_arr(arr)
    assert res == 28


def test_sum_arr_base_case():
    arr = [2]
    res = sum_arr(arr)
    assert res == 2


def test_sum_arr_empty_array():
    arr = []
    res = sum_arr(arr)
    assert res == 0
