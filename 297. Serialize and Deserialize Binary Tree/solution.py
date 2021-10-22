from typing import List, Optional, Dict, Set, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    COMMA = ","
    SEMICOLON = ";"

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        pre_order: List[str] = list()
        in_order: List[str] = list()
        post_order: List[str] = list()

        self.traverse(root, pre_order, in_order, post_order)

        return self.SEMICOLON.join([self.COMMA.join(pre_order), self.COMMA.join(in_order)])

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if len(data) == 0:
            return None

        orders: List[str] = data.split(self.SEMICOLON)

        pre_order: List[str] = orders[0].split(self.COMMA)
        in_order: List[str] = orders[1].split(self.COMMA)
        post_order: List[str] = list()

        return self.deserialize_pre_in(pre_order, in_order)

    def deserialize_pre_in(self, pre_order: List[str], in_order: List[str]) -> Optional[TreeNode]:

        if len(pre_order) == 0:
            return None

        root = TreeNode()

        root.val = pre_order[0]

        root_inorder_index = in_order.index(root.val)

        root.left = self.deserialize_pre_in(pre_order[1: root_inorder_index + 1], in_order[:root_inorder_index])
        root.right = self.deserialize_pre_in(pre_order[root_inorder_index + 1:], in_order[root_inorder_index + 1:])

        return root

    def traverse(self, root: Optional[TreeNode], pre_order: List[str], in_order: List[str], post_order: List[str]):
        if root is None:
            return
        pre_order.append(str(root.val))
        self.traverse(root.left, pre_order, in_order, post_order)
        in_order.append(str(root.val))
        self.traverse(root.right, pre_order, in_order, post_order)
        post_order.append(str(root.val))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

