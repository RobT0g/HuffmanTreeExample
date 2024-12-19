import typing
import matplotlib.pyplot as plt
from DataStructures import *
import networkx as nx
import numpy as np
import json

class HuffmanTree:
    def __init__(self, text:str, balance:bool=True):
        self.originalText:str = text
        self.root = None
        self.basicBinaryText = ''
        self.huffmanBinaryText = ''
        self.huffmanDictionary = {}
        self.weightDictionary = {}
        if balance: 
            self.balanceTree()
            self.mapDictionary()

    def balanceTree(self):
        count:dict = HuffmanTree.getCharacterCount(self.originalText)
        orderedAmounts = BalancedList()
        characterPos:typing.List[Node] = []

        def helperAdd(v:str, index:int):
            #print([None if i is None else i.value for i in characterPos], v.value, v.weight, index)
            if characterPos[index] is None:
                characterPos[index] = v
            else: 
                helperAdd(v, index+1)

        for i in count: 
            orderedAmounts.insertOrdered(count[i])
            characterPos.append(None)

        #print(orderedAmounts.getList())

        for i in count:
            check = orderedAmounts.checkContain(count[i])
            helperAdd(Node(i, count[i]), check[1])
        
        while len(characterPos) > 1:
            #print([(i.value, i.weight) for i in characterPos])
            newNode = Node(None, characterPos[0].weight + characterPos[1].weight)
            newNode.assignLeft(characterPos[0])
            newNode.assignRight(characterPos[1])

            characterPos.pop(0)
            characterPos.pop(0)
            orderedAmounts.dropVal(0)
            orderedAmounts.dropVal(0)

            newNodePos = orderedAmounts.insertOrdered(newNode.weight)
            characterPos.insert(newNodePos[1], newNode)
        
        self.root = characterPos[0]

    def calculateConversionDictionary(self):
        self.mapDictionary()
        with open('HuffmanDictionary.json', 'w') as file:
            json.dump(self.huffmanDictionary, file, indent=4)

    def mapDictionary(self, currentStep:Node|None=None, binaryString:str=''):
        if currentStep is None:
            currentStep = self.root
        if currentStep.getLeftBranch() is None and currentStep.getRightBranch() is None:
            self.huffmanDictionary[currentStep.value] = binaryString
            self.weightDictionary[currentStep.value] = currentStep.weight
            return
        self.mapDictionary(currentStep.getLeftBranch(), binaryString+'0')
        self.mapDictionary(currentStep.getRightBranch(), binaryString+'1')

    def convertIntoBinary(self) -> str:
        self.basicBinaryText = ''
        for i in self.originalText:
            self.basicBinaryText += HuffmanTree.convertFromCharToBinary(i)
        return self.basicBinaryText

    def convertIntoHuffmanBinary(self) -> str:
        self.huffmanBinaryText = ''
        for i in self.originalText:
            self.huffmanBinaryText += self.huffmanDictionary[i]
        return self.huffmanBinaryText

    def plotTreeBasic(self, currentStep:Node|None = None, level:int=0):
        if currentStep is None:
            currentStep = self.root
        
        print(f'{"-"*level}{currentStep.getSignature()}')
        
        if currentStep.getRightBranch() is None and currentStep.getLeftBranch() is None:
            return
        
        self.plotTreeBasic(currentStep.getLeftBranch(), level+1)
        self.plotTreeBasic(currentStep.getRightBranch(), level+1)

    def plotTreeWithNetworkx(self):
        graph = nx.Graph()
        graph.add_node(self.root.getSignature())
        self.mapTreeWithNetworkx(graph, self.root)

        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")
        plt.title("Huffman Tree")
        plt.show()

    def mapTreeWithNetworkx(self, graph:nx.Graph, currentStep:Node):
        if currentStep.getRightBranch() is None and currentStep.getLeftBranch() is None:
            return
        
        graph.add_node(currentStep.getLeftBranch().getSignature())
        graph.add_edge(currentStep.getSignature(), currentStep.getLeftBranch().getSignature())
        self.mapTreeWithNetworkx(graph, currentStep.getLeftBranch())

        graph.add_node(currentStep.getRightBranch().getSignature())
        graph.add_edge(currentStep.getSignature(), currentStep.getRightBranch().getSignature())
        self.mapTreeWithNetworkx(graph, currentStep.getRightBranch())

    def getDefaultBinaryText(self) -> str:
        return ' '.join(HuffmanTree.convertFromCharToBinary(c) for c in self.originalText)

    def getCharacterCount(text: str) -> typing.Dict[str, int]:
        count = {}
        for i in text:
            if count.get(i, None) is None:
                count[i] = 1
            else:
                count[i] += 1
        return count

    def convertFromCharToBinary(value:str) -> str:
        return format(ord(value), '08b')

    def convertFromBinaryToChar(value:str) -> int:
        return chr(int(value, 2))

    def convertBack(self) -> str:
        currentNode = self.root
        convertedText = ''
        for i in self.huffmanBinaryText:
            if i == '0':
                currentNode = currentNode.getLeftBranch()
            else:
                currentNode = currentNode.getRightBranch()

            if currentNode.getLeftBranch() is None and currentNode.getRightBranch() is None:
                convertedText += currentNode.value
                currentNode = self.root

        return convertedText


class HuffmanBinaryStringConverter:
    def restoreSavedTree(folderName:str):
        huffmanDictionary = {}
        with open(f'Examples/{folderName}/HuffmanDictionary.json', 'r') as file:
            huffmanDictionary = json.load(file)

        weightDictionary = {}
        with open(f'Examples/{folderName}/WeightDictionary.json', 'r') as file:
            weightDictionary = json.load(file)
        
        text = ''
        with open(f'Examples/{folderName}/text.txt', 'r') as file:
            text = file.read()

        binaryText = ''
        with open(f'Examples/{folderName}/text_binary.txt', 'r') as file:
            binaryText = file.read()

        huffmanText = ''
        with open(f'Examples/{folderName}/text_binary_huffman.txt', 'r') as file:
            huffmanText = file.read()

        actualTree = Node(None, 0)
        for i in huffmanDictionary:
            currentNode = actualTree
            string = huffmanDictionary[i]
            #print(string)

            for j in huffmanDictionary[i]:
                if j == '0':
                    #print('L', end='')
                    if currentNode.getLeftBranch() is None:
                        blankNode = Node(None, 0)
                        currentNode.assignLeft(blankNode)
                        currentNode = blankNode
                    else:
                        currentNode = currentNode.getLeftBranch()

                else:
                    #print('R', end='')
                    if currentNode.getRightBranch() is None:
                        blankNode = Node(None, 0)
                        currentNode.assignRight(blankNode)
                        currentNode = blankNode
                    else:
                        currentNode = currentNode.getRightBranch()

            currentNode.value = i
            currentNode.weight = weightDictionary[i]
            #print(f' - {currentNode.value} = {currentNode.weight}')

        translatedText = ''
        currentNode = actualTree

        for i in huffmanText:
            if i == '0':
                currentNode = currentNode.getLeftBranch()

            else:
                currentNode = currentNode.getRightBranch()

            if currentNode.getLeftBranch() is None and currentNode.getRightBranch() is None:
                translatedText += currentNode.value
                currentNode = actualTree
                continue

        
        print(translatedText)


def runTestingForFolder(folderName:str):
    print(f'\n\n----- {folderName} Test -----')
    text = ''
    with open(f'Examples/{folderName}/text.txt', 'r') as file:
        text = file.read()
    tree = HuffmanTree(text)

    with open(f'Examples/{folderName}/HuffmanDictionary.json', 'w') as file:
        json.dump(tree.huffmanDictionary, file, indent=4)

    with open(f'Examples/{folderName}/WeightDictionary.json', 'w') as file:
        json.dump(tree.weightDictionary, file, indent=4)

    huffmanResult = tree.convertIntoHuffmanBinary()
    with open(f'Examples/{folderName}/text_binary_huffman.txt', 'w') as file:
        file.write(huffmanResult)
    
    binaryResult = tree.convertIntoBinary()
    with open(f'Examples/{folderName}/text_binary.txt', 'w') as file:
        file.write(binaryResult)

    print(f'Original String: {len(text)} characters')
    print(f'ASCII Binary String: {len(binaryResult)} bits')
    print(f'Huffman Binary String: {len(huffmanResult)} bits')

    #print(tree.convertBack())

def restore():
    HuffmanBinaryStringConverter.restoreSavedTree('bee_movie')

if __name__ == '__main__':
    runTestingForFolder('bee_movie')
    runTestingForFolder('lorem_ipsum')
    runTestingForFolder('autosar')
    #HuffmanBinaryStringConverter.restoreSavedTree('bee_movie')
    #HuffmanBinaryStringConverter.restoreSavedTree('lorem_ipsum')
    #HuffmanBinaryStringConverter.restoreSavedTree('autosar')
