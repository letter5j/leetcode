from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

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

