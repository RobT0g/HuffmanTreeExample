import typing
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import json

class Node:
    def __init__(self, value:str|None=None, weight:int=0):
        self.value:str|None = value
        self.weight:int = weight
        self.__left:Node|None = None
        self.__right:Node|None = None
    
    def assignLeft(self, newNode:'Node') -> None:
        'Pass a Node to be assigned to the left branch of the current Node'
        if not isinstance(newNode, Node):
            raise TypeError('Branches can only have a Node assigned')
        self.__left:Node = newNode
    
    def assignRight(self, newNode: 'Node') -> None:
        'Pass a Node to be assigned to the right branch of the current Node'
        if not isinstance(newNode, Node):
            raise TypeError('Branches can only have a Node assigned')
        self.__right = newNode

    def getLeftBranch(self) -> 'Node':
        'Returns the Node assigned to the left branch'
        return self.__left
    
    def getRightBranch(self) -> 'Node':
        'Returns the Node assigned to the right branch'
        return self.__right

    def getSignature(self) -> str:
        'Returns the Node signature which is "{weight} - {value}"'
        return f'{self.weight} - {self.value}'

    def __str__(self) -> str:
        return self.getSignature()

    def toJSONFile(self, fileName: str) -> None:
        'Creates a JSON string and saves it into the specified file'
        with open(fileName, 'w') as file:
            json.dump(self.JSONDictHelper(self), file, default=lambda x: x.__dict__, indent=4)

    @staticmethod
    def JSONDictHelper(currentStep:'Node') -> dict|list:
        'Recursive function to create a dictionary with the Node information'
        if currentStep.getLeftBranch() is None and currentStep.getRightBranch() is None:
            return [currentStep.value, currentStep.weight]
        return {
            '': [
                [currentStep.value, currentStep.weight],
                currentStep.JSONDictHelper(currentStep.getLeftBranch()),
                currentStep.JSONDictHelper(currentStep.getRightBranch())
            ]
        }

    @staticmethod
    def fromJSONFile(fileName: str) -> 'Node':
        'Reads a JSON file and returns a Node object'
        with open(fileName, 'r') as file:
            return Node.recursiveRebuildFromDict(json.loads(file.read()))

    @staticmethod
    def recursiveRebuildFromDict(currentStep:dict) -> 'Node':
        if type(currentStep) is list: 
            return Node(currentStep[0], currentStep[1])
        
        actualNode = Node(currentStep[""][0][0], currentStep[""][0][1])
        actualNode.assignLeft(Node.recursiveRebuildFromDict(currentStep[""][1]))
        actualNode.assignRight(Node.recursiveRebuildFromDict(currentStep[""][2]))

        return actualNode

    def plotTreeBasic(self, currentStep:'Node' = None, level:int=0):
        if currentStep is None:
            currentStep = self
        
        print(f'{"-"*level}{currentStep.getSignature()}')
        
        if currentStep.getRightBranch() is None and currentStep.getLeftBranch() is None:
            return
        
        self.plotTreeBasic(currentStep.getLeftBranch(), level+1)
        self.plotTreeBasic(currentStep.getRightBranch(), level+1)

    def plotTreeWithNetworkx(self):
        graph = nx.Graph()
        graph.add_node(self.getSignature())
        self.mapTreeWithNetworkx(graph, self)

        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")
        plt.title("Huffman Tree")
        plt.show()

    def mapTreeWithNetworkx(self, graph:nx.Graph, currentStep:'Node'):
        if currentStep.getRightBranch() is None and currentStep.getLeftBranch() is None:
            return
        
        graph.add_node(currentStep.getLeftBranch().getSignature())
        graph.add_edge(currentStep.getSignature(), currentStep.getLeftBranch().getSignature())
        self.mapTreeWithNetworkx(graph, currentStep.getLeftBranch())

        graph.add_node(currentStep.getRightBranch().getSignature())
        graph.add_edge(currentStep.getSignature(), currentStep.getRightBranch().getSignature())
        self.mapTreeWithNetworkx(graph, currentStep.getRightBranch())


class BalancedList:
    def __init__(self, initialList:list=[]):
        self.__list:np.ndarray = np.array(initialList)
        self.__list.sort()

    def checkContain(self, value:str|int) -> typing.Tuple[bool, int]:
        pos = self.__list.searchsorted(value, side='left')
        
        if self.__list[pos] != value:
            return False, pos, pos
        
        endAt = self.__list.searchsorted(value, side='right')
        return True, pos, endAt-1
        
    def insertOrdered(self, value:str|int) -> typing.Tuple[bool, int, int]:
        pos = self.checkContain(value)
        if pos[0]:
            pos = pos[2]+1
        else:
            pos = pos[2]
        
        self.__list = np.insert(self.__list, pos, value)
        return True, pos, pos
    
    def dropVal(self, index:int):
        self.__list = np.delete(self.__list, index)

    def getList(self) -> list:
        return self.__list.copy()
    
    def __str__(self) -> str:
        return str(self.__list)

