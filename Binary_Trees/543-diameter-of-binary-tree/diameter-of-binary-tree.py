# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0

        def height(Node):
            if not Node:
                return 0
            left_height = height(Node.left)
            right_height = height(Node.right)
            self.dia = max(self.dia, left_height + right_height)
            return 1 + max(left_height, right_height)

        height(root)
        return self.dia