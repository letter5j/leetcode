from typing import Optional, Dict, Set


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    history: Dict[int, bool]

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        if head.next is None:
            return False
        if head.val in self.history:
            return True
        else:
            self.history[head.val] = True
            return self.hasCycle(head.next)
