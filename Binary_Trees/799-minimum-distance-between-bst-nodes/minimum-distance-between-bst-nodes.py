# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        self.pred = None
        self.inorder(root)
        return self.ans

    def inorder(self, node:TreeNode):
        if node is None:
            return
        self.inorder(node.left)

        if self.pred is not None:
            self.ans = min(self.ans, node.val - self.pred)
        self.pred = node.val
        self.inorder(node.right)
