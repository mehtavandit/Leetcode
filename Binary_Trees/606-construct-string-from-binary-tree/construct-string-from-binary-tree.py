# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if node is None:
                return ""

            result = str(node.val)
            
            if node.left or node.right:
                result += "(" + dfs(node.left) + ")"

            if node.right:
                result += "(" + dfs(node.right) + ")"


            return result

        return dfs(root)
