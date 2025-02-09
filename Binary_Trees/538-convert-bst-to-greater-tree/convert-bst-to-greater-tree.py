# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if node is None:
                return 0

            dfs(node.right)

            node.val += self.carryone
            self.carryone = node.val 

            dfs(node.left)

        
        self.carryone = 0
        dfs(root)
        return root
