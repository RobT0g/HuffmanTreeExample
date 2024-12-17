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
def sample_binary_characters_test() -> typing.Dict[str, str]:
    return {
        'input': 'abcsd',
        'output': '01100001 01100010 01100011 01110011 01100100'
    }

@pytest.fixture
def sample_not_balanced_tree(sample_binary_characters_test) -> HuffmanTree:
    return HuffmanTree(sample_binary_characters_test['input'])

def test_convert_single_char_to_binary():
    assert HuffmanTree.convertFromCharToBinary('a') == '01100001'

def test_convert_single_binary_to_char():
    assert HuffmanTree.convertFromBinaryToChar('01100001') == 'a'

def test_convert_initial_text_to_binary(sample_binary_characters_test, sample_not_balanced_tree):
    assert sample_not_balanced_tree.getDefaultBinaryText() == sample_binary_characters_test['output']