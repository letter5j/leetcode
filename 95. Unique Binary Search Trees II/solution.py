from typing import List, Optional, Dict, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.generate_trees(1, n)

    def generate_trees(self, left: int, right: int) -> List[Optional[TreeNode]]:
        if left > right:
            return [None]

        trees: List[TreeNode] = list()
        for i in range(left, right + 1):
            left_trees = self.generate_trees(left, i - 1)
            right_trees = self.generate_trees(i + 1, right)
            for lt in left_trees:
                for rt in right_trees:
                    root = TreeNode()
                    root.left = lt
                    root.right = rt
                    root.val = i
                    trees.append(root)
        return trees
