# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        root.right = self.invertBT(root.right)
        return self.isSame(root.left, root.right)

    def invertBT(self, node):
        if node is None:
            return node
        
        node.left, node.right = node.right, node.left
        node.left = self.invertBT(node.left)
        node.right = self.invertBT(node.right)

        return node

    def isSame(self, node1, node2):
        if (node1 is None) and (node2 is None):
            return True
        if (node1 is None) or (node2 is None) or (node1.val != node2.val):
            return False
        
        return self.isSame(node1.left, node2.left) and self.isSame(node1.right, node2.right)