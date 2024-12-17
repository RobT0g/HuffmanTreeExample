import typing

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

class BalancedList:
    def __init__(self, initialList:list=[]):
        self.__list:list = initialList
        self.__list.sort()

    def checkContain(self, value:str|int) -> typing.Tuple[bool, int]:
        return BalancedList.__binary_search_helper(self.__list, value, 0, len(self.__list) - 1)

    def insertOrdered(self, value:str|int, repeatable:bool=True) -> typing.Tuple[bool, int, int]:
        check = self.checkContain(value)
        self.__list.insert(check[1], value)
        if not check[0]:
            return True, check[1], check[2]
        return True, check[1], check[2]+1
    
    def dropVal(self, index:int):
        self.__list.pop(index)

    def getList(self) -> list:
        return self.__list[:]
    
    def binary_search(lst, value):
        return BalancedList.__binary_search_helper(lst, value, 0, len(lst) - 1)
    
    def __binary_search_helper(lst, value, low, high) -> typing.Tuple[bool, int, int]:
        if low > high:
            if lst[low] < value:
                return False, low, low
            return False, high, high
        
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
            if lst[low] < value:
                return False, low, low
            return False, high, high

        if value < lst[mid]:
            return BalancedList.__binary_search_helper(lst, value, low, mid - 1)
        
        return BalancedList.__binary_search_helper(lst, value, mid + 1, high)


class HuffmanTree:
    def __init__(self, text:str, balance:bool=True):
        self.originalText:str = text
        self.root = None
        if balance: self.balanceTree()

    def balanceTree(self):
        def helperAdd(v:str, index:int):
            if characterPos[index] is None:
                characterPos[index] = v
            else: helperAdd(v, index+1)

        count:dict = HuffmanTree.getCharacterCount(self.originalText)
        orderedAmounts = BalancedList()
        characterPos:typing.List[Node] = []

        for i in count: 
            orderedAmounts.insertOrdered(count[i])
            characterPos.append(None)

        for i in count:
            check = orderedAmounts.checkContain(count[i])
            helperAdd(Node(i, count[i]), check[0])
        
        for i in range(len(characterPos)-1, 0, -1):
            newNode = Node(None, characterPos[i].weight + characterPos[i-1].weight)
            newNode.assignLeft(characterPos[i-1])
            newNode.assignRight(characterPos[i])

            characterPos.pop(i)
            characterPos.pop(i-1)
            orderedAmounts.dropVal(i)
            orderedAmounts.dropVal(i-1)

            newNodePos = orderedAmounts.insertOrdered(newNode.weight)
            characterPos.insert(newNodePos[0], newNode)
        
        self.root = characterPos[0]

    def plotTree(self):
        pass
        #t = Tree(self.stringifyTree(self.root))
        #t.show()

    def stringifyTree(self, currentStep:Node):
        if currentStep.getRightBranch() is None and currentStep.getLeftBranch is None:
            return f'{currentStep.weight} - {currentStep.value}'
        stringified = '('
        if currentStep.getRightBranch() is not None:
            stringified += f'{self.stringifyTree(currentStep.getRightBranch())},'
        else:
            stringified += 'None,'
        if currentStep.getLeftBranch() is not None:
            stringified += f'{self.stringifyTree(currentStep.getLeftBranch())})'
        else:
            stringified += 'None)'
        return stringified

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
