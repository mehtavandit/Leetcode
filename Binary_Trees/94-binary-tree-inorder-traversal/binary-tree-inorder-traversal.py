# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # recursive
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     result = []
    #     self.helper(root, result)
    #     return result

    # def helper(self, node: Optional[TreeNode], result: List[int]):
    #     if node is None:
    #         return
    #     self.helper(node.left, result)
    #     result.append(node.val)
    #     self.helper(node.right, result)

    # iterative

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        stack = []
        inorder = []

        while True:

            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                inorder.append(current.val)
                current=current.right
            else:
                break

        return inorder
