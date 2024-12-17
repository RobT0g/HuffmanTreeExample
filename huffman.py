import typing
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Node:
    def __init__(self, value:str|None, weight:int):
        self.value:str|None = value
        self.weight:int = weight
        self.__left:Node|None = None
        self.__right:Node|None = None
    
    def assignLeft(self, newNode:'Node') -> None:
        self.__left = newNode
    
    def assignRight(self, newNode: 'Node') -> None:
        self.__right = newNode

    def getLeftBranch(self) -> 'Node':
        return self.__left
    
    def getRightBranch(self) -> 'Node':
        return self.__right

    def getSignature(self) -> str:
        if self.value is None: return f'{self.weight} - '
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


    def __binary_search_helper(lst, value, low, high) -> typing.Tuple[bool, int, int]:
        #print(lst, value, low, high)
        if low > high:
            insertPos = BalancedList.__findWhereToInsert(lst, value, low, high)
            return False, insertPos, insertPos

        mid = (low + high) // 2

        if lst[mid] == value:
            boundaries = [mid, mid]

            for step in range(mid, -1, -1):
                if lst[step] == value: continue
                boundaries[0] = step+1
                break

            for step in range(mid, len(lst)):
                if lst[step] == value: continue
                boundaries[1] = step-1
                break

            return True, boundaries[0], boundaries[1]
        
        if low == high:
            insertPos = BalancedList.__findWhereToInsert(lst, value, low, high)
            return False, insertPos, insertPos

        if value < lst[mid]:
            return BalancedList.__binary_search_helper(lst, value, low, mid - 1)
        
        return BalancedList.__binary_search_helper(lst, value, mid + 1, high)


class HuffmanTree:
    def __init__(self, text:str, balance:bool=True):
        self.originalText:str = text
        self.root = None
        if balance: self.balanceTree()

    def balanceTree(self):
        count:dict = HuffmanTree.getCharacterCount(self.originalText)
        orderedAmounts = BalancedList()
        characterPos:typing.List[Node] = []

        def helperAdd(v:str, index:int):
            print([None if i is None else i.value for i in characterPos], v.value, v.weight, index)
            if characterPos[index] is None:
                characterPos[index] = v
            else: 
                helperAdd(v, index+1)

        for i in count: 
            orderedAmounts.insertOrdered(count[i])
            characterPos.append(None)

        print(orderedAmounts.getList())

        for i in count:
            check = orderedAmounts.checkContain(count[i])
            helperAdd(Node(i, count[i]), check[1])
        
        while len(characterPos) > 1:
            newNode = Node(None, characterPos[0].weight + characterPos[1].weight)
            newNode.assignLeft(characterPos[0])
            newNode.assignRight(characterPos[1])

            characterPos.pop(0)
            characterPos.pop(1)
            orderedAmounts.dropVal(0)
            orderedAmounts.dropVal(1)

            newNodePos = orderedAmounts.insertOrdered(newNode.weight)
            characterPos.insert(newNodePos[0], newNode)
        
        self.root = characterPos[0]

    def plotTree(self):
        graph = nx.Graph()
        graph.add_node(self.root.getSignature())
        self.mapTree(graph, self.root)

        pos = nx.spring_layout(graph, seed=42)
        nx.draw(graph, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")
        plt.title("Huffman Tree")
        plt.show()

    def mapTree(self, graph:nx.Graph, currentStep:Node):
        if currentStep.getRightBranch() is None and currentStep.getLeftBranch is None:
            return
        
        graph.add_node(currentStep.getLeftBranch().getSignature())
        graph.add_edge(currentStep.getSignature(), currentStep.getLeftBranch().getSignature())
        self.mapTree(currentStep.getLeftBranch())

        graph.add_node(currentStep.getRightBranch().getSignature())
        graph.add_edge(currentStep.getSignature(), currentStep.getRightBranch().getSignature())
        self.mapTree(currentStep.getRightBranch())

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


if __name__ == '__main__':
    # Usage
    tree = HuffmanTree('iasogsdioasonaspvasdcpoiasnvaplsklmcojsiscpkasmca')
    tree.plotTree()
    '''tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.in_order_traversal(tree.root)'''
