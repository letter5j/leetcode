from typing import List, Optional, Dict, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def numTrees(self, n: int) -> int:

        count: Dict[int, int] = dict()
        return self.num_trees(n, count)

    def num_trees(self, n: int, count: Dict[int, int]) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in count:
            return count[n]
        trees_sum = 0
        for root in range(1, n + 1):
            trees_sum = trees_sum + self.num_trees(root - 1, count) * self.num_trees(n - root, count)
        if trees_sum not in count:
            count[n] = trees_sum
        return trees_sum
