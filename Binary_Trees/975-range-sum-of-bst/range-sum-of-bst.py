# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    #     return self.helper(root, low, high)

    # def helper(self, node:TreeNode, low, high):
    #     if node is None:
    #         return 0

    #     x = node.val
    #     current_sum = 0

    #     if low <= x and x <= high:
    #         current_sum += x

    #     current_sum += self.helper(node.left, low, high)
    #     current_sum += self.helper(node.right, low, high)

    #     return current_sum

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            if not node:
                return
            if low<=node.val<=high:
                self.total += node.val
                dfs(node.left)
                dfs(node.right)
            elif node.val < low:
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)

        self.total = 0
        dfs(root)
        return self.total

