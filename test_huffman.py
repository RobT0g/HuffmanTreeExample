from huffman import *
import pytest
import typing

## Preset Parameters
sampleData = [
    ('bee_movie', HuffmanTree('bee_movie', False)), 
    ('lorem_ipsum', HuffmanTree('lorem_ipsum', False))
] 

def __getSampleText(folderPath: str) -> str:
    return open(f'Examples/{folderPath}/text.txt', 'r').read()

@pytest.mark.parametrize('sample_folder, sample_huffman_tree', sampleData)
def test_can_instantiate_huffman_tree(sample_folder:str, sample_huffman_tree:HuffmanTree):
    assert sample_huffman_tree
    assert isinstance(sample_huffman_tree, HuffmanTree)
    assert sample_huffman_tree.folderPath == sample_folder

@pytest.mark.parametrize('sample_folder, sample_huffman_tree', sampleData)
def test_is_reading_text_file(sample_folder:str, sample_huffman_tree:HuffmanTree):
    assert sample_huffman_tree.originalText == __getSampleText(sample_folder)

@pytest.mark.parametrize('sample_folder, sample_huffman_tree', sampleData)
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
        ('haters gonna hate', '0110100001100001011101000110010101110010011100110010000001100111011011110110111001101110011000010010000001101000011000010111010001100101')

    ]
)
def test_can_convert_char_to_binary(characters:str, binary:str):
    assert HuffmanTree.nonHuffman_convertFromCharToBinary(characters) == binary

@pytest.mark.parametrize(
    ('characters'),
    [
        None,
        {},
        []
    ]
)
def test_invalid_character_raises_error(characters:any):
    with pytest.raises(TypeError):
        HuffmanTree.nonHuffman_convertFromCharToBinary(characters)

def test_empty_character_raises_error():
    with pytest.raises(ValueError):
        HuffmanTree.nonHuffman_convertFromCharToBinary('')

@pytest.mark.parametrize(
    ('binary', 'characters'),
    [
        ('01100001', 'a'),
        ('01100010', 'b'),
        ('00100000', ' '),
        ('00100001', '!'),
        ('01101111011010010110101101100001011100110110111001100100', 'oikasnd'),
        ('0110100001100001011101000110010101110010011100110010000001100111011011110110111001101110011000010010000001101000011000010111010001100101', 'haters gonna hate')
    ]
)
def test_can_convert_binary_to_char(binary:str, characters:str):
    assert HuffmanTree.nonHuffman_convertFromBinaryToChar(binary) == characters

@pytest.mark.parametrize(
    ('binary'),
    [
        None,
        {},
        []
    ]
)
def test_invalid_binary_raises_error(binary:any):
    with pytest.raises(TypeError):
        HuffmanTree.nonHuffman_convertFromBinaryToChar(binary)

@pytest.mark.parametrize(
    ('binary'),
    [
        pytest.param('', id='EmptyString'),
        pytest.param('011000010', id='TooLongString'),
        pytest.param('0110000', id='TooShortString'),        
    ]
)
def test_invalid_binary_raises_error_with_an_invalid_string(binary:str):
    with pytest.raises(ValueError):
        HuffmanTree.nonHuffman_convertFromBinaryToChar(binary)

def __navigationWeightTester(node:Node, levelWeight:typing.List[typing.List[int]], currentLevel=0) -> int:
    if len(levelWeight) < currentLevel+1:
        levelWeight.append([])
    
    if len(levelWeight[currentLevel]) == 0:
        levelWeight[currentLevel].append(node.weight)
        levelWeight[currentLevel].append(node.weight)
    
    elif levelWeight[currentLevel][0] > node.weight:
        levelWeight[currentLevel][0] = node.weight
    
    elif levelWeight[currentLevel][1] < node.weight:
        levelWeight[currentLevel][1] = node.weight
    
    if node.getLeftBranch() is None and node.getRightBranch() is None:
        return
    
    assert node.weight == node.getLeftBranch().weight + node.getRightBranch().weight
    
    __navigationWeightTester(node.getLeftBranch(), levelWeight, currentLevel+1)
    __navigationWeightTester(node.getRightBranch(), levelWeight, currentLevel+1)    

@pytest.mark.parametrize('sample_folder, sample_huffman_tree', sampleData)
def test_can_balance_tree(sample_folder:str, sample_huffman_tree:HuffmanTree):
    sample_huffman_tree.balanceTree()
    assert sample_huffman_tree
    assert sample_huffman_tree.root

    levelWeights = []
    __navigationWeightTester(sample_huffman_tree.root, levelWeights)

    for i in range(len(levelWeights)-1):
        assert levelWeights[i][0] >= levelWeights[i+1][1]


