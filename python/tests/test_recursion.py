import scripts.recursion as re


def test_factorial():
    res = re.factorial(5)
    assert res == 120


def test_factorial_base_case():
    res = re.factorial(1)
    assert res == 1


def test_sum_arr():
    arr = [2, 3, 5, 7, 11]
    res = re.sum_arr(arr)
    assert res == 28


def test_sum_arr_base_case():
    arr = [2]
    res = re.sum_arr(arr)
    assert res == 2


def test_sum_arr_empty_array():
    arr = []
    res = re.sum_arr(arr)
    assert res == 0


def test_count_list_items():
    arr = ["a", "b", "c", "d", "e"]
    res = re.count_list_items(arr)
    assert res == 5


def test_count_list_items_single_item():
    arr = ["a"]
    res = re.count_list_items(arr)
    assert res == 1


def test_count_list_items_empty_array():
    arr = []
    res = re.count_list_items(arr)
    assert res == 0
