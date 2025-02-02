# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        refval = root.val
        count = self.helper(root, refval)
        return count

    def helper(self, node, refval):
        if node is None:
            return 0

        count = 1 if node.val >= refval else 0
        refval = max(node.val, refval)

        count += self.helper(node.left, refval)
        count += self.helper(node.right, refval)

        return count

        
