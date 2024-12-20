from DataStructures import *
import typing
import json

class HuffmanTree:
    def __init__(self, folderPath:str, balance:bool=True, strict:bool=False) -> None:
        if strict:
            self.folderPath = folderPath
        else:
            self.folderPath = f'Examples/{folderPath}'

        self.originalText = ''
        with open(f'{self.folderPath}/text.txt', 'r') as file:
            self.originalText = file.read()
        
        self.root:Node = None
        self.__huffmanDictionary:typing.Dict[str, str] = {}

        if balance:
            self.balanceTree()
    
    def balanceTree(self):
        count = self.getWeightDictionary()
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
        self.mapDictionary(self.root)

    def mapDictionary(self, currentStep:Node|None, binaryString:str=''):
        if currentStep.getLeftBranch() is None and currentStep.getRightBranch() is None:
            self.__huffmanDictionary[currentStep.value] = binaryString
            return
        
        self.mapDictionary(currentStep.getLeftBranch(), binaryString+'0')
        self.mapDictionary(currentStep.getRightBranch(), binaryString+'1')

    def getBinaryString(self) -> str:
        return self.nonHuffman_convertFromCharToBinary(self.originalText)

    def getHuffmanBinaryString(self) -> str:
        binaryString = ''
        for i in self.originalText:
            binaryString += self.__huffmanDictionary[i]
        return binaryString

    def getHuffmanDictionary(self) -> typing.Dict[str, str]:
        return self.__huffmanDictionary

    def getWeightDictionary(self) -> typing.Dict[str, int]:
        return self.getCharacterCount(self.originalText)

    def saveToFolder(self) -> None:
        with open(f'{self.folderPath}/HuffmanDictionary.json', 'w') as file:
            json.dump(self.__huffmanDictionary, file, indent=4)
        
        with open(f'{self.folderPath}/text_binary.txt', 'w') as file:
            file.write(self.getBinaryString())
        
        with open(f'{self.folderPath}/text_binary_huffman.txt', 'w') as file:
            file.write(self.getHuffmanBinaryString())
        
        with open(f'{self.folderPath}/WeightDictionary.json', 'w') as file:
            json.dump(self.getWeightDictionary(), file, indent=4)

    def getSummaryReport(self) -> str:
        summary = f'\n\n------ Running Huffman Tree on ------{self.folderPath}\n'
        summary += f'Original text length: {len(self.originalText)}\n'
        summary += f'Binary text length: {len(self.getBinaryString())}\n'
        summary += f'Huffman text length: {len(self.getHuffmanBinaryString())}\n'
        print(summary)

        summaryDictionary = {}
        summaryDictionary['Original text length'] = len(self.originalText)
        summaryDictionary['Binary text length'] = len(self.getBinaryString())
        summaryDictionary['Huffman text length'] = len(self.getHuffmanBinaryString())

        return summaryDictionary

    def restoreHuffmanString(self) -> str:
        huffmanBinaryString = self.getHuffmanBinaryString()
        currentStep = self.root
        restoredString = ''
        for i in huffmanBinaryString:
            if i == '0':
                currentStep = currentStep.getLeftBranch()
            else:
                currentStep = currentStep.getRightBranch()
            
            if currentStep.getLeftBranch() is None and currentStep.getRightBranch() is None:
                restoredString += currentStep.value
                currentStep = self.root
        
        return restoredString

    @staticmethod
    def getCharacterCount(text: str) -> typing.Dict[str, int]:
        '''Returns a dictionary of the count of each character in the text'''
        
        if type(text) != str:
            raise TypeError('Input must be a string')
        if len(text) == 0:
            raise ValueError('Input must not be empty')
        
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
    def recoverFromFolder(folderPath: str, strict:bool=False) -> 'HuffmanTree':
        tree = HuffmanTree(folderPath, False, strict)
        with open(f'{tree.folderPath}/HuffmanDictionary.json', 'r') as file:
            tree.__huffmanDictionary = json.load(file)
        
        weightDictionary = {}
        with open(f'{tree.folderPath}/WeightDictionary.json', 'r') as file:
            weightDictionary = json.load(file)

        tree.root = Node(None, 0)
        currentStep = tree.root
        for i in tree.__huffmanDictionary:
            for j in tree.__huffmanDictionary[i]:
                if j == '0':
                    if currentStep.getLeftBranch() is None:
                        currentStep.assignLeft(Node(None, 0))
                    currentStep = currentStep.getLeftBranch()

                else:
                    if currentStep.getRightBranch() is None:
                        currentStep.assignRight(Node(None, 0))
                    currentStep = currentStep.getRightBranch()
            
            currentStep.value = i
            currentStep.weight = weightDictionary[i]
            currentStep = tree.root
        
        def weightAssigner(currentStep:Node) -> int:
            if currentStep.getLeftBranch() is None and currentStep.getRightBranch() is None:
                return currentStep.weight
            currentStep.weight = weightAssigner(currentStep.getLeftBranch()) + weightAssigner(currentStep.getRightBranch())
            return currentStep.weight
        
        weightAssigner(tree.root)

        return tree
        


if __name__ == '__main__':
    testingTree = HuffmanTree('bee_movie', True, False)