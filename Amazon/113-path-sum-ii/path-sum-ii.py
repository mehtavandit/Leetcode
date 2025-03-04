# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        current_sum = 0
        result = []
        self.helper(root, current_sum, targetSum,[], result)
        return result
    
    def helper(self,node, current_sum, targetSum, path, result):
        if node is None:
            return

        current_sum += node.val
        path.append(node.val)

        if current_sum == targetSum and (node.left == None) and (node.right == None):
            result.append(path[:])

        if node.left:
            self.helper(node.left, current_sum, targetSum, path , result)
        if node.right:
            self.helper(node.right, current_sum, targetSum, path , result)

        path.pop()