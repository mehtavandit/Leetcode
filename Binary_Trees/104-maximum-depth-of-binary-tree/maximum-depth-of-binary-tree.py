# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        height = 0

        q = Queue()

        q.put(root)

        while not q.empty():
            size = q.qsize()

            for i in range(size):
                front = q.get()

                if front.left is not None:
                    q.put(front.left)

                if front.right is not None:
                    q.put(front.right)

            height += 1

        return height 


