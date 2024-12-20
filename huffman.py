from DataStructures import *
import typing
import json

class HuffmanTree:
    def __init__(self, folderPath:str, balance:bool=True):
        self.folderPath = folderPath
        self.originalText = open(f'Examples/{folderPath}/text.txt', 'r').read()
        self.root:Node = None
        if balance:
            self.balanceTree()
    
    def balanceTree(self):
        count = HuffmanTree.getCharacterCount(self.originalText)
        orderedAmounts = BalancedList()
        characterPos:typing.List[Node] = []
        
        for i in count:
            pos = orderedAmounts.insertOrdered(count[i])
            characterPos.insert(pos[1], Node(i, count[i]))
        
        for i in range(len(characterPos)-1):
            newNode = Node(None, characterPos[0].weight + characterPos[1].weight)
            newNode.assignLeft(characterPos[0])
            newNode.assignRight(characterPos[1])
            
            characterPos.pop(0)
            characterPos.pop(0)
            orderedAmounts.dropVal(0)
            orderedAmounts.dropVal(0)
            
            pos = orderedAmounts.insertOrdered(newNode.weight)
            characterPos.insert(pos[2], newNode)
        
        self.root = characterPos[0]

    def mapDictionary(self, currentStep:Node|None=None, binaryString:str=''):
        pass

    def getBinaryString(self) -> str:
        pass

    def getHuffmanBinaryString(self) -> str:
        pass

    def getHuffmanDictionary(self) -> typing.Dict[str, str]:
        pass

    def getWeightDictionary(self) -> typing.Dict[str, int]:
        pass

    def saveToFolder(self) -> None:
        pass

    @staticmethod
    def getCharacterCount(text: str) -> typing.Dict[str, int]:
        '''Returns a dictionary of the count of each character in the text'''
        count = {}
        for char in text:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        return count

    @staticmethod
    def nonHuffman_convertFromCharToBinary(char: str) -> str:
        '''Converts a string of characters to a binary string'''
        if type(char) != str:
            raise TypeError('Input must be a string')
        if len(char) == 0:
            raise ValueError('Input must not be empty')
        convertedString = ''
        for i in char:
            convertedString += format(ord(i), '08b')
        return convertedString

    @staticmethod
    def nonHuffman_convertFromBinaryToChar(binary: str) -> str:
        '''Converts a binary string to a string of characters (Must be a multiple of 8)'''
        int(binary, 2)
        if len(binary) % 8 != 0:
            raise ValueError('Input must be a multiple of 8')
        return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

    @staticmethod
    def recoverFromFolder(folderPath: str) -> 'HuffmanTree':
        pass


