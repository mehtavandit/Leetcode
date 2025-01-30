# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root is None:
            return []

        q = deque()
        l_to_r = True

        q.append(root)

        while q:
            size = len(q)
            level = []
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if not l_to_r:
                level.reverse()

            result.append(level)
            l_to_r = not l_to_r

        return result