from typing import List, Optional, Dict, Set, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ancestor: Optional[TreeNode] = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.traverse(root, p, q)

        return self.ancestor

    def traverse(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> (bool, bool):

        if root is None or self.ancestor is not None:
            return False, False

        find_p_left, find_q_left = self.traverse(root.left, p, q)
        find_p_right, find_q_right = self.traverse(root.right, p, q)
        find_p = find_p_left or find_p_right
        find_q = find_q_left or find_q_right
        if (find_p_left and find_q_right) or (find_q_left and find_p_right) or (find_p and root.val == q.val) or (
                find_q and root.val == p.val):
            if self.ancestor is None:
                self.ancestor = root
        return root.val == p.val or find_p_left or find_p_right, root.val == q.val or find_q_left or find_q_right
