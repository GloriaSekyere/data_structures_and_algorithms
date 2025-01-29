import pytest
from script.singly_linked_list import SinglyLinkedList


@pytest.fixture
def empty_sll():
    return SinglyLinkedList()


@pytest.fixture
def sll_single():
    sll = SinglyLinkedList()
    sll.append(3)
    return sll


@pytest.fixture
def sll():
    sll = SinglyLinkedList()
    data = [3, 24, 17, 1, 58, 58, -5]
    for d in data:
        sll.append(d)
    return sll


def test_create_sll():
    sll = SinglyLinkedList()
    assert isinstance(sll, SinglyLinkedList)


def test_append(empty_sll):
    empty_sll.append(5)
    assert empty_sll.find(5) == True


def test_find_target_exists(sll):
    assert sll.find(1) == True


def test_find_empty_list(empty_sll):
    assert empty_sll.find(13) == False


def test_find_target_does_not_exist(sll):
    assert sll.find(100) == False


def test_insert_at_index_0(sll):
    sll.insert(0, 20)
    assert sll.find(20) == True


def test_insert_at_random_index(sll):
    sll.insert(5, 44)
    assert sll.find(44) == True


def test_insert_index_beyond_list_length(sll_single):
    sll_single.insert(5, 90)
    assert sll_single.find(90) == True


def test_remove(sll):
    assert sll.remove(1) is True


def test_remove_from_empty_sll(empty_sll):
    assert empty_sll.remove(1) is False


def test_remove_target_does_not_exist(sll):
    assert sll.remove(100) is False


def test_get_min(sll):
    assert sll.get_min() == -5


def test_get_min_empty_list(empty_sll):
    assert empty_sll.get_min() == None


def test_get_min_list_with_one_item(sll_single):
    assert sll_single.get_min() == 3


def test_get_max(sll):
    assert sll.get_max() == 58


def test_get_max_empty_list(empty_sll):
    assert empty_sll.get_max() == None


def test_get_max_list_with_one_item(sll_single):
    assert sll_single.get_max() == 3


def test_get_length(sll):
    assert sll.get_length() == 7


def test_get_length_empty_list(empty_sll):
    assert empty_sll.get_length() == 0


def test_get_length_single_list(sll_single):
    assert sll_single.get_length() == 1
