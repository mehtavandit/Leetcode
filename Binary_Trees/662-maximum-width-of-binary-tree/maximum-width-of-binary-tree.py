# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        q = deque([(root, 0)])

        while q:
            size = len(q)
            _, firstindex = q[0]
            _, lastindex = q[-1]

            max_width = max(max_width, lastindex - firstindex + 1)

            for i in range(size):
                node, index = q.popleft()

                if node.left:
                    q.append((node.left, 2 * index ))
                if node.right:
                    q.append((node.right, 2 * index + 1))


        return max_width

                