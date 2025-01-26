# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot is None:
            return True

        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
    
    def isSameTree(self, p:TreeNode, q:TreeNode):
        if (p is None) and (q is None):
            return True

        if (p is None) or (q is None) or (p.val != q.val):
            return False

        value1 = self.isSameTree(p.left, q.left)
        value2 = self.isSameTree(p.right, q.right)

        return value1 and value2
