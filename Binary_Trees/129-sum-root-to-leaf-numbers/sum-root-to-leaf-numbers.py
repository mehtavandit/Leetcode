# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, string=""):
            if node is None:
                return

            string += str(node.val)

            if node.left is None and node.right is None:
                x = int(string)
                self.sum += x

            helper(node.left, string)
            helper(node.right, string)
            

        self.sum = 0
        helper(root)
        return self.sum