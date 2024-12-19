import typing
import pytest
from DataStructures import *
import json

#Node tests
@pytest.fixture
def sample_tree_schema() -> list:    
    treeSchema = {
        "": [
            ['A', 27],
            {
                "": [
                    [None, 3],
                    ['R', 9],
                    ['B', 1],
                ]
            }, 
            {
                "": [
                    ['G', 6],
                    ['C', 1],
                    {
                        "": [
                            ['l', 13],
                            ['D', 7], 
                            [' ', 15]
                        ]
                    }
                ]
            }
        ]
    }

    return treeSchema

@pytest.fixture
def sample_tree_created_with_original(sample_tree_schema) -> Node:
    return Node.recursiveRebuildFromDict(sample_tree_schema)

@pytest.fixture
def sample_tree_created_from_json_string(sample_tree_schema) -> Node:
    return Node.recursiveRebuildFromDict(json.loads(json.dumps(sample_tree_schema)))

def test_root_node_signature_correctness(sample_tree_schema:dict, sample_tree_created_with_original:Node):
    assert Node(sample_tree_schema[""][0][0], sample_tree_schema[""][0][1]).getSignature() == sample_tree_created_with_original.getSignature()

def test_root_left_branch_signature_correctness(sample_tree_schema:list, sample_tree_created_with_original:Node):
    leftBranch = sample_tree_schema[""][1]
    if type(leftBranch) is dict:
        leftBranch = leftBranch[""][0]
    leftBranch = Node(leftBranch[0], leftBranch[1])

    assert leftBranch.getSignature() == sample_tree_created_with_original.getLeftBranch().getSignature()

def test_root_right_branch_signature_correctness(sample_tree_schema:list, sample_tree_created_with_original:Node):
    rightBranch = sample_tree_schema[""][2]
    if type(rightBranch) is dict:
        rightBranch = rightBranch[""][0]
    rightBranch = Node(rightBranch[0], rightBranch[1])

    assert rightBranch.getSignature() == sample_tree_created_with_original.getRightBranch().getSignature()

def test_assign_none_value_on_left_branch(sample_tree_created_with_original:Node):
    with pytest.raises(TypeError):
        sample_tree_created_with_original.assignLeft(None)

def test_assign_none_value_on_right_branch(sample_tree_created_with_original:Node):
    with pytest.raises(TypeError):
        sample_tree_created_with_original.assignRight(None)

def test_save_tree_into_json_file(sample_tree_created_with_original:Node):
    sample_tree_created_with_original.toJSONFile('sample_tree.json')
    with open('sample_tree.json', 'r') as file:
        assert json.load(file) == sample_tree_created_with_original.JSONDictHelper(sample_tree_created_with_original)



#BalancedList tests
@pytest.fixture
def sample_ordered_list() -> BalancedList:
    originalList = [1, 3, 2, 5, 12, 5, 12, 7, 13, 17, 5, 4, 4, 5, 4, 9, 6, 8, 4, 3, 41]
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
    #print(pos, ordered)
    assert pos[1]
    assert ordered[pos[1]] == 10
    if pos[1] > 0:
        assert ordered[pos[1]-1] <= 10
    if pos[2] < len(ordered)-1:
        assert ordered[pos[1]+1] >= 10
