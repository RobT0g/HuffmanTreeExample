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

def __getSampleText(folderPath: str) -> str:
    return open(f'Examples/{folderPath}/text.txt', 'r').read()

def test_can_instantiate_huffman_tree(sample_folder:str, sample_huffman_tree:HuffmanTree):
    assert sample_huffman_tree
    assert isinstance(sample_huffman_tree, HuffmanTree)
    assert sample_huffman_tree.folderPath == sample_folder

def test_is_reading_text_file(sample_folder:str, sample_huffman_tree:HuffmanTree):
    assert sample_huffman_tree.originalText == getSampleText(sample_folder)

def test_can_get_character_count(sample_folder:str, sample_huffman_tree:HuffmanTree):
    sample_text = __getSampleText(sample_folder)
    count = HuffmanTree.getCharacterCount(sample_text)
    actualCount = {}
    for char in sample_text:
        if char in actualCount:
            actualCount[char] += 1
        else:
            actualCount[char] = 1
    for i in actualCount:
        assert count[i] == actualCount[i]
    
@pytest.mark.parametrize(
    ('characters', 'binary'),
    [
        ('a', '01100001'),
        ('b', '01100010'),
        (' ', '00100000'),
        ('!', '00100001'),
        ('oikasnd', '01101111011010010110101101100001011100110110111001100100'),
        ('haters gonna hate', '01101000011000010111010001100101011100110111010000100000011001110110000101101110011011110111010001101000011000010111010001100101')
    ]
)
def test_can_convert_char_to_binary(characters:str, binary:str):
    assert HuffmanTree.nonHuffman_convertFromCharToBinary(characters) == binary

@pytest.mark.parametrize(
    ('characters'),
    [
        (''),
        (None),
        ({}),
        ([])
    ]
)
def test_invalid_character_raises_error(characters:any):
    with pytest.raises(ValueError):
        HuffmanTree.nonHuffman_convertFromCharToBinary(characters)


