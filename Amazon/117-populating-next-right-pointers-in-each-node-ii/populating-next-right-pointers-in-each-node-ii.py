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
    def connect(self, root: 'Node') -> 'Node':
        # if root is None:
        #     return

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

        current = root

        while current:
            dummy = Node(0)
            prev = dummy
            temp = current

            while temp:
                if temp.left:
                    prev.next = temp.left
                    prev = prev.next
                 
                if temp.right:
                    prev.next = temp.right
                    prev = prev.next

                temp = temp.next

            current = dummy.next
            dummy.next = None


        return root