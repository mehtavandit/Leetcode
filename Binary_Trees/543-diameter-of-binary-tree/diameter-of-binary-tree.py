# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        self.helper(root, diameter)
        return diameter[0]  

    def helper(self, node: TreeNode, diameter: list) -> int:
        if node is None:
            return 0
        
        left_height = self.helper(node.left, diameter)
        right_height = self.helper(node.right, diameter)
        diameter[0] = max(diameter[0], left_height + right_height)
        
        return 1 + max(left_height, right_height)
