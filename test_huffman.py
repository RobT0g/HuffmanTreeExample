from huffman import *
import pytest
import typing
import os

## Preset Parameters
sampleData = [
    ('bee_movie', HuffmanTree('bee_movie', False, False)), 
    ('lorem_ipsum', HuffmanTree('lorem_ipsum', False, False))
]
sampleFolders = [i[0] for i in sampleData]
sampleTrees = [i[1] for i in sampleData]

def __getSampleText(folderPath: str) -> str:
    return open(f'Examples/{folderPath}/text.txt', 'r').read()

@pytest.mark.parametrize('sample_folder, sample_huffman_tree', sampleData)
def test_can_instantiate_huffman_tree(sample_folder:str, sample_huffman_tree:HuffmanTree):
    assert sample_huffman_tree
    assert isinstance(sample_huffman_tree, HuffmanTree)
    assert sample_huffman_tree.folderPath == f'Examples/{sample_folder}'

@pytest.mark.parametrize('sample_folder, sample_huffman_tree', sampleData)
def test_is_reading_text_file(sample_folder:str, sample_huffman_tree:HuffmanTree):
    assert sample_huffman_tree.originalText == __getSampleText(sample_folder)

@pytest.mark.parametrize('sample_folder', sampleFolders)
def test_can_get_character_count(sample_folder:str):
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

@pytest.mark.parametrize('sample_huffman_tree', sampleTrees)
def test_can_get_instance_character_count(sample_huffman_tree:HuffmanTree):
    count = sample_huffman_tree.getWeightDictionary()
    actualCount = HuffmanTree.getCharacterCount(sample_huffman_tree.originalText)

    for i in actualCount:
        assert count[i] == actualCount[i]

@pytest.mark.parametrize(
    'characters', 
    [
        1,
        [],
        {},
        None
    ]
)
def test_invalid_characters_raises_error(characters:any):
    with pytest.raises(TypeError):
        HuffmanTree.getCharacterCount(characters)

def test_empty_characters_raises_error():
    with pytest.raises(ValueError):
        HuffmanTree.getCharacterCount('')

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

def __navigationWeightTester(node:Node, levelWeight:typing.List[typing.List[int]], currentLevel=0) -> None:
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

def __isTreeBalanced(tree:HuffmanTree) -> None:
    assert tree
    assert tree.root

    levelWeights = []
    __navigationWeightTester(tree.root, levelWeights)

    for i in range(len(levelWeights)-1):
        assert levelWeights[i][0] >= levelWeights[i+1][1]

@pytest.mark.parametrize('sample_huffman_tree', sampleTrees)
def test_can_balance_tree(sample_huffman_tree:HuffmanTree):
    sample_huffman_tree.balanceTree()
    __isTreeBalanced(sample_huffman_tree)

@pytest.mark.parametrize('sample_folder', sampleFolders)
def test_tree_is_balanced_at_constructor(sample_folder):
    sample_huffman_tree = HuffmanTree(sample_folder, True)
    __isTreeBalanced(sample_huffman_tree)

def __checkDictionary(dictionary:typing.Dict[str, str], tree:Node) -> None:
    for i in dictionary:
        currentNode = tree

        for j in dictionary[i]:
            assert j in ['0', '1']
            
            if j == '0':
                currentNode = currentNode.getLeftBranch()
            else:
                currentNode = currentNode.getRightBranch()
            
        assert currentNode.value == i

@pytest.mark.parametrize('sample_huffman_tree', sampleTrees)
def test_can_map_dictionary(sample_huffman_tree:HuffmanTree):
    sample_huffman_tree.balanceTree()
    
    huffmanDictionary = sample_huffman_tree.getHuffmanDictionary()
    assert huffmanDictionary

    __checkDictionary(huffmanDictionary, sample_huffman_tree.root)

@pytest.mark.parametrize('sample_folder', sampleFolders)
def test_can_map_dictionary_at_constructor(sample_folder):
    sample_huffman_tree = HuffmanTree(sample_folder, True)
    huffmanDictionary = sample_huffman_tree.getHuffmanDictionary()
    assert huffmanDictionary

    __checkDictionary(huffmanDictionary, sample_huffman_tree.root)

@pytest.mark.parametrize('sample_huffman_tree', sampleTrees)
def test_can_get_binary_string(sample_huffman_tree:HuffmanTree):
    sample_huffman_tree.balanceTree()
    binaryString = sample_huffman_tree.getBinaryString()
    assert binaryString

    for i in binaryString:
        assert i in ['0', '1']

    convertedBinary = HuffmanTree.nonHuffman_convertFromCharToBinary(sample_huffman_tree.originalText)
    assert binaryString == convertedBinary 

@pytest.mark.parametrize('sample_huffman_tree', sampleTrees)
def test_can_get_huffman_binary_string(sample_huffman_tree:HuffmanTree):
    sample_huffman_tree.balanceTree()
    huffmanBinaryString = sample_huffman_tree.getHuffmanBinaryString()
    assert huffmanBinaryString

    for i in huffmanBinaryString:
        assert i in ['0', '1']

    actualBinary = ''
    dictionary = sample_huffman_tree.getHuffmanDictionary()
    for i in sample_huffman_tree.originalText:
        actualBinary += dictionary[i]
    
    assert huffmanBinaryString == actualBinary

@pytest.mark.parametrize('sample_folder', sampleFolders)
def test_can_save_into_the_folder_pre_created_samples_probably_will_always_pass(sample_folder):
    sample_huffman_tree = HuffmanTree(sample_folder, True)
    sample_huffman_tree.saveToFolder()

    assert open(f'Examples/{sample_folder}/text_binary.txt', 'r').read()
    assert open(f'Examples/{sample_folder}/text_binary_huffman.txt', 'r').read()
    assert open(f'Examples/{sample_folder}/HuffmanDictionary.json', 'r').read()
    assert open(f'Examples/{sample_folder}/WeightDictionary.json', 'r').read()

@pytest.mark.parametrize(
    ('sample_folder'),
    [
        ('SampleFolderWithAnUniqueName'),
        ('AnotherSampleFolderWithAnUniqueName')
    ]
)
def test_can_pass_a_strict_folder_location(sample_folder, tmp_path):
    d = tmp_path / sample_folder
    d.mkdir()
    p = d / 'text.txt'
    p.write_text("Dont care")
    
    sample_huffman_tree = HuffmanTree(str(d), False, True)
    assert sample_huffman_tree

@pytest.mark.parametrize(
    ('sample_folder', 'sample_content'),
    [
        ('SampleFolderWithAnUniqueName', 'SampleContentWithAnUniqueName'),
        ('AnotherSampleFolderWithAnUniqueName', 'AnotherSampleContentWithAnUniqueName')
    ]
)
def test_can_save_into_folder_with_a_temp_file(sample_folder, sample_content, tmp_path):
    d = tmp_path / f'{sample_folder}'
    d.mkdir()
    p = d / f'text.txt'
    p.write_text(sample_content)
    
    sample_huffman_tree = HuffmanTree(str(d), True, True)
    sample_huffman_tree.saveToFolder()

    files = os.listdir(d)
    for file in files:
        print(file)

    assert open(d / 'text_binary.txt', 'r').read()
    assert open(d / 'text_binary_huffman.txt', 'r').read()
    assert open(d / 'HuffmanDictionary.json', 'r').read()
    assert open(d / 'WeightDictionary.json', 'r').read()

@pytest.mark.parametrize('sample_folder', sampleFolders)
def test_are_saved_files_correct(sample_folder):
    sample_huffman_tree = HuffmanTree(sample_folder, True)
    sample_huffman_tree.saveToFolder()
