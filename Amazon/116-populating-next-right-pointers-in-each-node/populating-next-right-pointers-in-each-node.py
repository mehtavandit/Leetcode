"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # if not root:
        #     return None

        # q = deque([root])

        # while q:
        #     size = len(q)
        #     prev = None

        #     for _ in range(size):
        #         node = q.popleft()
        #         if prev:
        #             prev.next = node
        #         prev = node

        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        #     prev.next = None

        
        # return root

        #TC :- O(n) as it visits each node once and Space complexity O(n) due to queue storage

        if not root:
            return None

        leftmost = root

        while leftmost.left:
            current = leftmost

            while current:
                current.left.next = current.right

                if current.next:
                    current.right.next = current.next.left

                current = current.next

            
            leftmost = leftmost.left

        return root

