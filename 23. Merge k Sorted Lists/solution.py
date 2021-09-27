# ref: https://docs.python.org/zh-tw/3/library/heapq.html
import math
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MaxPriorityQueue:
    pq: list[int] = []

    def parent(self, root: int) -> int:
        return math.floor(root / 2)

    def left(self, root: int) -> int:
        return root * 2

    def right(self, root: int) -> int:
        return root * 2 + 1

    def max(self) -> int:
        return self.pq[1]

    def insert(self, root: int):
        self.pq.append(root)
        self.swim(len(self.pq))

    def delete_max(self):
        self.exchange(self.pq[1], self.pq[-1])

        self.pq.remove(-1)

        self.sink(1)

    def swim(self, index: int):
        parent_index: int = self.parent(index)
        while index > 1 and self.pq[parent_index] < self.pq[index]:
            self.exchange(parent_index, index)
            index = parent_index

    def exchange(self, index: int, index1: int):
        temp: int = self.pq[index]
        self.pq[index] = self.pq[index1]
        self.pq[index] = temp


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        result = ListNode(0)
        pointer = result
        pointer1 = l1
        pointer2 = l2

        while pointer1 is not None and pointer2 is not None:

            if pointer1.val <= pointer2.val:
                pointer.next = pointer1
                pointer1 = pointer1.next
            else:
                pointer.next = pointer2
                pointer2 = pointer2.next
            pointer = pointer.next

        if pointer1 is not None:
            pointer.next = pointer2
        if pointer2 is not None:
            pointer.next = pointer1

        return result.next
