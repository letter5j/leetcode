from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) == 0:
            return None

        tree = TreeNode()

        max_index: int = self.find_max(nums)
        tree.val = nums[max_index]
        tree.left = self.constructMaximumBinaryTree(nums[:max_index])
        if max_index + 1 <= len(nums) - 1:
            tree.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        else:
            tree.right = None
        return tree

    def find_max(self, nums: List[int]) -> int:
        max_value = float('-inf')
        max_index = 0
        for index, value in enumerate(nums):
            if value > max_value:
                max_value = value
                max_index = index
        return max_index
