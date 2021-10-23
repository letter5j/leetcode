from typing import List, Optional, Dict, Set, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    COMMA = ","
    NULL = "#"

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

        return self.COMMA.join(pre_order)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if len(data) == 0:
            return None


        pre_order: List[str] = data.split(self.COMMA)
        in_order: List[str] = data.split(self.COMMA)
        post_order: List[str] = data.split(self.COMMA)

        return self.deserialize_pre(pre_order)

    def deserialize_pre(self, pre_order: List[str]) -> Optional[TreeNode]:

        if len(pre_order) == 0:
            return None
        value = pre_order.pop(0)
        if value == "#":
            return None
        root = TreeNode()

        root.val = value

        root.left = self.deserialize_pre(pre_order)
        root.right = self.deserialize_pre(pre_order)
        return root

    def traverse(self, root: Optional[TreeNode], pre_order: List[str], in_order: List[str], post_order: List[str]):
        if root is None:
            pre_order.append(self.NULL)
            in_order.append(self.NULL)
            post_order.append(self.NULL)
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

