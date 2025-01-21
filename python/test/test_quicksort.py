from script.quicksort import quicksort


def test_quicksort():
    arr = [10, 5, 2, 3]
    res = quicksort(arr)
    assert res == sorted(arr)


def test_quicksort_empty_array():
    arr = []
    res = quicksort(arr)
    assert res == arr


def test_quicksort_single_item():
    arr = [10]
    res = quicksort(arr)
    assert res == arr


def test_quicksort_negative_items():
    arr = [-10, -5, -2, -3]
    res = quicksort(arr)
    assert res == sorted(arr)


def test_quicksort_positive_and_negative_items():
    arr = [-10, -5, -2, -3, 10, 5, 2, 3]
    res = quicksort(arr)
    assert res == sorted(arr)


def test_quicksort_same_items():
    arr = [4, 4, 4]
    res = quicksort(arr)
    assert res == sorted(arr)
