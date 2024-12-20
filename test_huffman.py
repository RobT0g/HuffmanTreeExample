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

def getSampleText(folderPath: str) -> str:
    return open(f'Examples/{folderPath}/text.txt', 'r').read()

def test_can_instantiate_huffman_tree(sample_folder:str, sample_huffman_tree:HuffmanTree):
    assert sample_huffman_tree
    assert isinstance(sample_huffman_tree, HuffmanTree)
    assert sample_huffman_tree.folderPath == sample_folder

def test_is_reading_text_file(sample_folder:str, sample_huffman_tree:HuffmanTree):
    assert sample_huffman_tree.originalText == getSampleText(sample_folder)

def test_can_get_character_count(sample_folder:str, sample_huffman_tree:HuffmanTree):
    sample_text = getSampleText(sample_folder)
    count = HuffmanTree.getCharacterCount(sample_text)
    actualCount = {}
    for char in sample_text:
        if char in actualCount:
            actualCount[char] += 1
        else:
            actualCount[char] = 1
    for i in actualCount:
        assert count[i] == actualCount[i]
    

