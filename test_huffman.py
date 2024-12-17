from huffman import *
import pytest
import typing

@pytest.fixture
def sample_tree_fixture() -> Node:
    nodes = {'root': 'a', 'left': 'b', 'right': 'c'}
    return nodes

def test_create_initial_node(sample_tree_fixture):
    initialNode = Node(sample_tree_fixture['root'])
    assert initialNode.getValue() == sample_tree_fixture['root']
    assert initialNode.getLeftBranch() is None
    assert initialNode.getRightBranch() is None

def test_assign_left_branch(sample_tree_fixture):
    initialNode = Node(sample_tree_fixture['root'])
    leftNode = Node(sample_tree_fixture['left'])
    initialNode.assignLeft(leftNode)
    assert initialNode.getLeftBranch() == leftNode
    assert initialNode.getLeftBranch().getValue() == sample_tree_fixture['left']

def test_assign_right_branch(sample_tree_fixture):
    initialNode = Node(sample_tree_fixture['root'])
    rightNode = Node(sample_tree_fixture['right'])
    initialNode.assignRight(rightNode)
    assert initialNode.getRightBranch() == rightNode
    assert initialNode.getRightBranch().getValue() == sample_tree_fixture['right']

@pytest.fixture
def sample_huffman_tree():
    pass


