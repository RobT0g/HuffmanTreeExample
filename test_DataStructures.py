import typing
import pytest
from DataStructures import *

#Node tests
@pytest.fixture
def sample_nodes() -> Node:
    treeSchema = [
        ('A', 27)
        [
            (None, 3)
            ('R', 9)
            ('B', 1),
        ], [
            ('G', 6)
            ('C', 1),
            [
                ('l', 13)
                ('D', 7), 
                (' ', 15)
            ]
        ]
    ]

    def depthFirstNav(currentNode:Node, currentStep:tuple|list):
        if type(currentStep) is tuple: return
        
        leftNode = Node()
        if type(currentStep[0]) is tuple:
            leftNode = Node(currentStep[0][0], currentStep[0][1])
        
        currentNode.assignLeft(leftNode)
        depthFirstNav(leftNode, currentStep[0])

        rightNode = Node()
        if type(currentStep[1] is tuple):
            rightNode = Node(currentStep[1][0], currentStep[1][1])
        
        currentStep.assignRight(rightNode)
        depthFirstNav(currentStep[1])

    actualTree = Node()
    depthFirstNav(actualTree, treeSchema)
    return actualTree

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