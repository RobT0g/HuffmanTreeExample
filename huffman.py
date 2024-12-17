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

    def getList(self) -> list:
        return self.__list
    
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
        self.count = []
        self.root = None
        self.__balanceTree()

    def __balanceTree(self):
        pass

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
    tree = HuffmanTree()
    '''tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.in_order_traversal(tree.root)'''
