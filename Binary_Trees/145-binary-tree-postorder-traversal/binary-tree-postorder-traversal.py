# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #recursive
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, node: Optional[TreeNode], result: List[int]):
        if node is None:
            return
        self.helper(node.left, result)
        self.helper(node.right, result)
        result.append(node.val)

    # #using two stacks
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     stack1 = []
    #     stack2 = []

    #     postorder = []

    #     if root is None:
    #         return postorder

    #     stack1.append(root)

    #     while stack1:
    #         current = stack1.pop()

    #         stack2.append(current)

    #         if current.left is not None:
    #             stack1.append(current.left)
            
    #         if current.right is not None:
    #             stack1.append(current.right)

    #     while stack2:
    #         postorder.append(stack2.pop)

    #     return postorder