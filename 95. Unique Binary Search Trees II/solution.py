from typing import List, Optional, Dict, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        trees: Dict[str, TreeNode] = dict()

        nums: List[int] = [i for i in range(1, 10 + 1)]

        self.generate_trees(nums, trees)
        trees.
        return

    def generate_trees(self, nums: List[int], count: Dict[str, TreeNode]) -> List[Optional[TreeNode]]:
        if len(nums) == 0:
            return []
        #
        # if len(nums)n == 1:
        #     return [
        #         tr
        #     ]
        if n in count:
            return count[n]
        trees: List[TreeNode] = list()
        for root in range(1, n + 1):
            left_trees = self.generate_trees(root - 1, count)
            right_trees = self.generate_trees(n - root, count)
            tree_root: TreeNode = TreeNode()
            for lt in left_trees:
                for rt in right_trees:
                    tree_root.left = lt
                    tree_root.right = rt
                    trees.append(tree_root)
            trees_sum = trees_sum +
            *self.num_trees(n - root, count)
        if trees_sum not in count:
            count[n] = trees_sum
        return
