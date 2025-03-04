# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0

        def traverse(root):
            nonlocal total
            if root is None:
                return
            
            if root.left is not None and root.left.left is None and root.left.right is None:
                total += root.left.val

            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return total