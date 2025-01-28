# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        result  = self.helper(root)
        return result

    def helper(self, node):
        if not node.left and not node.right:
            return node.val == 1

        lresult = self.helper(node.left)
        rresult = self.helper(node.right)

        if node.val == 2:
            return lresult or rresult
        elif node.val == 3:
            return lresult and rresult

        

        