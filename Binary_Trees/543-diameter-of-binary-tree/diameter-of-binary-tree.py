# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Use a list to hold diameter so it's mutable
        diameter = [0]
        self.helper(root, diameter)
        return diameter[0]  # Return the first element of the list

    def helper(self, node: TreeNode, diameter: list) -> int:
        if node is None:
            return 0
        
        # Recur for left and right subtrees
        left_height = self.helper(node.left, diameter)
        right_height = self.helper(node.right, diameter)
        
        # Update the diameter (the longest path between any two nodes)
        diameter[0] = max(diameter[0], left_height + right_height)
        
        # Return the height of the current node
        return 1 + max(left_height, right_height)
