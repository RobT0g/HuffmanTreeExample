from huffman import *
import pytest
import typing

pytestmark = pytest.mark.parametrize(
    'sample_folder, sample_huffman_tree', 
    [
        ('bee_movie', HuffmanTree('bee_movie')), 
        ('lorem_ipsum', HuffmanTree('lorem_ipsum'))
    ]
)


'''class TestHuffmanTree(typing.NamedTuple):
    sample_folder: str
    sample_huffman_tree: HuffmanTree

@pytest.fixture
@pytest.mark.parametrize(
    'sample_folder, sample_huffman_tree', 
    [
        ('bee_movie', HuffmanTree('bee_movie')), 
        ('lorem_ipsum', HuffmanTree('lorem_ipsum'))
    ]
)
def sample_folder_and_tree(sample_folder, sample_huffman_tree) -> TestHuffmanTree:
    return TestHuffmanTree(sample_folder, sample_huffman_tree)'''

def test_can_instantiate_huffman_tree(sample_folder, sample_huffman_tree):
    assert sample_huffman_tree
    assert isinstance(sample_huffman_tree, HuffmanTree)
    assert sample_huffman_tree.folderPath == sample_folder

def test_is_reading_text_file(sample_folder, sample_huffman_tree):
    h = HuffmanTree('test')
    assert h.getCharacterCount('test.txt') == {'t': 2, 'e': 1, 's': 1}
