from old_huffman import *
import pytest
import typing

@pytest.fixture
def sample_tree_fixture() -> Node:
    nodes = {'root': 'a', 'left': 'b', 'right': 'c'}
    return nodes

def test_create_initial_node(sample_tree_fixture):
    initialNode = Node(sample_tree_fixture['root'], 10)
    assert initialNode.value == sample_tree_fixture['root']
    assert initialNode.getLeftBranch() is None
    assert initialNode.getRightBranch() is None
    assert initialNode.weight == 10

def test_assign_left_branch(sample_tree_fixture):
    initialNode = Node(sample_tree_fixture['root'], 0)
    leftNode = Node(sample_tree_fixture['left'], 0)
    initialNode.assignLeft(leftNode)
    assert initialNode.getLeftBranch() == leftNode
    assert initialNode.getLeftBranch().value == sample_tree_fixture['left']

def test_assign_right_branch(sample_tree_fixture):
    initialNode = Node(sample_tree_fixture['root'], 0)
    rightNode = Node(sample_tree_fixture['right'], 0)
    initialNode.assignRight(rightNode)
    assert initialNode.getRightBranch() == rightNode
    assert initialNode.getRightBranch().value == sample_tree_fixture['right']

@pytest.fixture
def sample_character_counter() -> typing.Tuple[str, typing.Dict[str, int]]:
    inputString = 'asofba acaacacahtrda'
    count = {}
    for i in inputString:
        if count.get(i, None) is None:
            count[i] = 1
        else:
            count[i] += 1
    return inputString, count

@pytest.fixture
def sample_binary_characters_test() -> typing.Dict[str, str]:
    return {
        'input': 'abcsd',
        'output': '01100001 01100010 01100011 01110011 01100100'
    }

@pytest.fixture
def sample_not_balanced_tree(sample_binary_characters_test) -> HuffmanTree:
    return HuffmanTree(sample_binary_characters_test['input'], False)

def test_convert_single_char_to_binary():
    assert HuffmanTree.convertFromCharToBinary('a') == '01100001'

def test_convert_single_binary_to_char():
    assert HuffmanTree.convertFromBinaryToChar('01100001') == 'a'

def test_convert_initial_text_to_binary(sample_binary_characters_test, sample_not_balanced_tree):
    assert sample_not_balanced_tree.getDefaultBinaryText() == sample_binary_characters_test['output']

def test_character_counter_correctness(sample_character_counter):
    string, count = sample_character_counter
    huffCount = HuffmanTree.getCharacterCount(string)
    for i in count:
        assert huffCount[i] == count[i]
