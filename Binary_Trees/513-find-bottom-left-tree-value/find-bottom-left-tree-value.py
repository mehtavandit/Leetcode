# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return []

        left_node = root.val

        q = deque()
        q.append(root)

        while q:
            size = len(q)
            result = []

            for i in range(size):
                node = q.popleft()

                result.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            left_node = result[0]


        return left_node

        