# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root,result)
        return result

    def helper(self, node:Optional[TreeNode], result:List[int]):
        if node is None:
            return

        self.helper(node.left, result)

        self.helper(node.right, result)

        result.append(node.val)

        