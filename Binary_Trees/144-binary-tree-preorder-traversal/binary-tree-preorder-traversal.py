# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # # recursive method
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     result = []
    #     self.helper(root, result)
    #     return result

    # def helper(self, node: Optional[TreeNode], result: List[int]):
    #     if node is None:
    #         return
    #     result.append(node.val)
    #     self.helper(node.left, result)
    #     self.helper(node.right, result)

    #iterative method

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       preorder = []
       if root is None:
         return preorder
       
       stack = []
       stack.append(root)
       
       while stack:
        node = stack.pop()
        preorder.append(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)
            
       return preorder

    

