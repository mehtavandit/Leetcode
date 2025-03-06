# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        boundary = []

        if root.left is not None or root.right is not None:
            boundary.append(root.val)

        boundary += self.getLeftBoundary(root.left)
        boundary += self.getLeaves(root)
        boundary += self.getRightBoundary(root.right)

        return boundary

    def getLeftBoundary(self, node):
        left_boundary = []
        while node:
            if node.left or node.right:
                left_boundary += [node.val]
            node = node.left if node.left else node.right
        print(left_boundary)
        return left_boundary

    def getRightBoundary(self, node):
        right_boundary = []
        while node:
            if node.left or node.right:
                right_boundary.append(node.val)
            node = node.right if node.right else node.left
        print(right_boundary)
        return right_boundary[::-1]

    def getLeaves(self, node):
        if not node:
            return []
        if node.left is None and node.right is None:
            return [node.val]
        return self.getLeaves(node.left) + self.getLeaves(node.right)