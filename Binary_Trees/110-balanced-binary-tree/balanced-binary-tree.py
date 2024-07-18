# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check_balance(root) != -1

    def check_balance(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        left_height = self.check_balance(node.left)
        if left_height == -1:
            return -1
        
        right_height = self.check_balance(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1