# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if root is None:
                return 0

            leftsum = dfs(root.left)
            rightsum = dfs(root.right)
            leftsum = max(0, leftsum) #don't want negative numbers
            rightsum = max(0, rightsum)

            res[0] = max(res[0], root.val + leftsum + rightsum)
            return root.val + max(leftsum, rightsum) #want to send maximum one up

        dfs(root)
        return res[0]