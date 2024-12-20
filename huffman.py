from DataStructures import *
import typing
import json

class HuffmanTree:
    def __init__(self, folderPath:str, balance:bool=True):
        self.folderPath = folderPath
        self.originalText = open(f'Examples/{folderPath}/text.txt', 'r').read()
    
    def balanceTree(self):
        pass

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
        count = {}
        for char in text:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        return count

    @staticmethod
    def nonHuffman_convertFromCharToBinary(char: str) -> str:
        'REMINDER: make this also work with an actual string, not just char'
        ord(char)
        convertedString = ''
        for i in char:
            convertedString += format(ord(i), '08b')
        return convertedString

    @staticmethod
    def nonHuffman_convertFromBinaryToChar(binary: str) -> str:
        'REMINDER: make this also work with an actual string, not just char'
        pass

    @staticmethod
    def recoverFromFolder(folderPath: str) -> 'HuffmanTree':
        pass


