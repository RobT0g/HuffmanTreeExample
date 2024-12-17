import typing

class Node:
    def __init__(self, value:str):
        self.__value:str = value
        self.__left:Node|None = None
        self.__right:Node|None = None

    def getValue(self) -> str:
        return self.__value
    
    def assignLeft(self, newNode:'Node') -> None:
        self.__left = newNode
    
    def assignRight(self, newNode: 'Node') -> None:
        self.__right = newNode

    def getLeftBranch(self) -> 'Node':
        return self.__left
    
    def getRightBranch(self) -> 'Node':
        return self.__right

class HuffmanTree:
    def __init__(self, text:str, balance:bool=True):
        self.originalText:str = text
        self.count = []
        self.root = None
        self.__balanceTree()

    def __balanceTree(self):
        pass

    def getDefaultBinaryText(self) -> str:
        return ' '.join(HuffmanTree.convertFromCharToBinary(c) for c in self.originalText)

    def convertFromCharToBinary(value:str) -> str:
        return format(ord(value), '08b')

    def convertFromBinaryToChar(value:str) -> int:
        return chr(int(value, 2))


if __name__ == '__main__':
    # Usage
    tree = HuffmanTree()
    '''tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.in_order_traversal(tree.root)'''
