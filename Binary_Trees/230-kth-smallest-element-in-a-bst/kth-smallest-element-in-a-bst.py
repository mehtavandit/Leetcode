# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self.inorder(root, result)
        return result[k-1]


    def inorder(self, node, result):
        if node is None:
            return
        
        self.inorder(node.left, result)

        result.append(node.val)

        self.inorder(node.right, result)