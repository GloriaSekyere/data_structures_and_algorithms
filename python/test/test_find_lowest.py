from script.find_lowest import find_lowest


def test_find_lowest():
    arr = [621, 279, 823, 694, 89, 198, 797]
    assert find_lowest(arr) == 89


def test_find_lowest_single_item():
    arr = [4]
    assert find_lowest(arr) == 4


def test_find_lowest_empty_array():
    arr = []
    assert find_lowest(arr) == None


def test_find_lowest_negative_integers():
    arr = [-621, -279, -823, -694, -89, -198, -797]
    assert find_lowest(arr) == -823


def test_find_lowest_positive_and_negative_integers():
    arr = [621, -279, 823, 694, -89, 198, -797]
    assert find_lowest(arr) == -797
