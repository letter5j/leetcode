import secrets
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:

        node = self.head
        size = 1
        random_chose = node.val
        while node is not None:
            random_value = secrets.randbelow(size)
            if random_value == 0:
                random_chose = node.val
            size = size + 1
            node = node.next
        return random_chose
   