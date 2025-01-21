from script.binary_search import binary_search


def test_binary_search_low_number_exsits():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = 3
    res = binary_search(arr, num)
    assert res == 3


def test_binary_search_high_number_exsits():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = 7
    res = binary_search(arr, num)
    assert res == 7


def test_binary_search_number_does_not_exsit():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = 13
    res = binary_search(arr, num)
    assert res == None
