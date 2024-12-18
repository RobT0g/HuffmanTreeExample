import typing
import pytest
from DataStructures import *

#Node tests
@pytest.fixture
def sample_tree_schema() -> list:    
    treeSchema = [
        ('A', 27),
        [
            (None, 3),
            ('R', 9),
            ('B', 1),
        ], [
            ('G', 6),
            ('C', 1),
            [
                ('l', 13),
                ('D', 7), 
                (' ', 15)
            ]
        ]
    ]

    return treeSchema

@pytest.fixture
def sample_nodes(sample_tree_schema) -> Node:
    def depthFirstNav(currentStep:tuple|list) -> Node:
        if type(currentStep) is tuple: 
            return Node(currentStep[0], currentStep[1])
        
        actualNode = Node(currentStep[0][0], currentStep[0][1])
        actualNode.assignLeft(depthFirstNav(currentStep[1]))
        actualNode.assignRight(depthFirstNav(currentStep[2]))

        return actualNode


    actualTree = depthFirstNav(sample_tree_schema)
    return actualTree

def test_root_node_signature_correctness(sample_tree_schema, sample_nodes):
    assert Node(sample_tree_schema[0][0], sample_tree_schema[0][1]).getSignature() == sample_nodes.getSignature()

def test_root_left_branch_signature_correctness(sample_tree_schema:list, sample_nodes:Node):
    leftBranch = sample_tree_schema[1]
    if type(leftBranch) is list:
        leftBranch = leftBranch[0]
    leftBranch = Node(leftBranch[0], leftBranch[1])

    assert leftBranch.getSignature() == sample_nodes.getLeftBranch().getSignature()

def test_root_right_branch_signature_correctness(sample_tree_schema:list, sample_nodes:Node):
    rightBranch = sample_tree_schema[2]
    if type(rightBranch) is list:
        rightBranch = rightBranch[0]
    rightBranch = Node(rightBranch[0], rightBranch[1])

    assert rightBranch.getSignature() == sample_nodes.getRightBranch().getSignature()

def test_assign_none_value_on_left_branch(sample_nodes:Node):
    with pytest.raises(TypeError):
        sample_nodes.assignLeft(None)

def test_assign_none_value_on_right_branch(sample_nodes:Node):
    with pytest.raises(TypeError):
        sample_nodes.assignRight(None)

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