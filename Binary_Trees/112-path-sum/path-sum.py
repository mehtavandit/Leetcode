# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        current_sum = 0
        status = self.helper(root, current_sum, targetSum)
        return status

    def helper(self, node:TreeNode, current_sum, target_sum):
        if node is None:
            return False

        current_sum += node.val

        if (current_sum == target_sum) and (node.left == None) and (node.right==None):
            return True

        lstatus = self.helper(node.left, current_sum, target_sum)
        rstatus = self.helper(node.right, current_sum, target_sum)

        return lstatus or rstatus
        