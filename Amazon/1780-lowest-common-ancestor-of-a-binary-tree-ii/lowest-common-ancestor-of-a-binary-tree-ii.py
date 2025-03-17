# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = self.LCA(root, p,q)

        if ans!=p and ans!=q:
            return ans

        if self.LCA(ans.left, p,q) or self.LCA(ans.right, p,q):
            return ans
        else:
            return None

    def LCA(self, node, p, q):
        if node is None:
            return

        if node == p or node == q:
            return node

        left = self.LCA(node.left, p, q)
        right = self.LCA(node.right,p,q)

        if left and right:
            return node
        
        if left:
            return left

        if right:
            return right


        