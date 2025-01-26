# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root) != -1

    def helper(self, node: TreeNode):
        if not node:
            return 0
        
        lheight = self.helper(node.left)

        if lheight == -1:
            return -1

        rheight = self.helper(node.right)

        if rheight == -1:
            return -1

        if abs(lheight - rheight) > 1:
            return -1
        
        return max(lheight, rheight) + 1