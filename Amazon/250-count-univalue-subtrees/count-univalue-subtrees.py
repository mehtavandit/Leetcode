# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node is None:
                return True, 0

            left_status, left_count = dfs(node.left)
            right_status, right_count = dfs(node.right)

            if not left_status or not right_status: #if left or right subtress are not univalue, this node is also not univalue 
                return False, left_count + right_count

            if (node.left and node.left.val != node.val) or (node.right and node.right.val != node.val):
                return False, left_count + right_count

            return True, left_count + right_count + 1

        _, count = dfs(root)
        return count