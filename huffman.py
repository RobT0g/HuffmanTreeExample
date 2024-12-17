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
    def __init__(self):
        self.root = None

    def getHuffmanTree(text:str) -> 'HuffmanTree':
        tree = HuffmanTree()

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)


if __name__ == '__main__':
    # Usage
    tree = HuffmanTree()
    '''tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.in_order_traversal(tree.root)'''
