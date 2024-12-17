from huffman import *
import pytest
import typing

@pytest.fixture
def sample_ordered_list() -> BalancedList:
    originalList = [1, 3, 2, 5, 12, 5, 12, 7, 13, 17]
    return BalancedList(originalList)

def test_element_is_present(sample_ordered_list):
    ordered = sample_ordered_list.getList()
    for i in range(len(ordered)):
        check = sample_ordered_list.checkContain(ordered[i])
        assert check[0]
        assert i >= check[1]
        assert i <= check[2]

def test_list_is_sorted(sample_ordered_list):
    ordered = sample_ordered_list.getList()
    for i in range(1, len(ordered)):
        assert ordered[i-1] <= ordered[i]

def test_inserted_at_right_ordered_pos(sample_ordered_list):
    pos = sample_ordered_list.insertOrdered(10, True)
    ordered = sample_ordered_list.getList()
    assert pos[1]
    assert ordered[pos[1]] == 10
    if pos[1] > 0:
        assert ordered[pos[1]-1] < 10
    if pos[2] < len(ordered)-1:
        assert ordered[pos[1]+1] > 10