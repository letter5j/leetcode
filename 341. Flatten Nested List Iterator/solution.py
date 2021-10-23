# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List


class NestedInteger:
    pass


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> List[NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    flatten_list: List[int] = list()

    def __init__(self, nestedList: [NestedInteger]):
        self.flatten_list = self.flatten(nestedList)

    def flatten(self, nested_list: List[NestedInteger]) -> List[int]:
        flatten_list: List[int] = list()
        for nested_integer in nested_list:

            if nested_integer.isInteger():
                flatten_list.append(nested_integer.getInteger())
            else:
                flatten_list = flatten_list + self.flatten(nested_integer.getList())
        return flatten_list

    def next(self) -> int:
        return self.flatten_list.pop(0)

    def hasNext(self) -> bool:

        return len(self.flatten_list) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
