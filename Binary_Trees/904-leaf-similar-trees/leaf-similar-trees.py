# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1 = []
        self.helper(root1, tree1)
        tree2 = []
        self.helper(root2, tree2)

        return tree1 == tree2

    def helper(self, node, array):
        if node is None:
            return

        if node.left is None and node.right is None:
            array.append(node.val)
        
        self.helper(node.left, array)
        self.helper(node.right, array)

        return array

