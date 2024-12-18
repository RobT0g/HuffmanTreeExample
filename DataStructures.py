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

class BalancedList:
    def __init__(self, initialList:list=[]):
        self.__list:np.ndarray = np.array(initialList)
        self.__list.sort()

    def checkContain(self, value:str|int) -> typing.Tuple[bool, int]:
        pos = self.__list.searchsorted(value)
        
        if self.__list[pos] != value:
            return False, pos, pos
        
        endAt = pos+1
        while True:
            if endAt >= len(self.__list):
                break
            if self.__list[endAt] > value:
                break
            endAt += 1
        return True, pos, endAt-1
        
    def insertOrdered(self, value:str|int, repeatable:bool=True) -> typing.Tuple[bool, int, int]:
        pos = self.__list.searchsorted(value)
        self.__list = np.insert(self.__list, pos, value)
        return True, pos, pos
    
    def dropVal(self, index:int):
        self.__list = np.delete(self.__list, index)

    def getList(self) -> list:
        return self.__list.copy()