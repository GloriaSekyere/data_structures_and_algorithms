from script.selection_sort import selection_sort


def test_selection_sort():
    arr = [3, 6, 8, 2, 1, 4, 7, 0, 9]
    result = selection_sort(arr)
    assert result == sorted(arr)


def test_selection_sort_empty_array():
    arr = []
    result = selection_sort(arr)
    assert result == []


def test_selection_sort_already_sorted_array():
    arr = [0, 1, 2, 3, 4, 5]
    result = selection_sort(arr)
    assert result == arr
