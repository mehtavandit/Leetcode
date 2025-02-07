from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        q = deque([root])
        counter = 0  

        while q:
            size = len(q)
            prev = None  

            for _ in range(size):
                node = q.popleft()

                
                if counter % 2 == 0:
                    if node.val % 2 == 0:  
                        return False
                    if prev is not None and node.val <= prev:  
                        return False

                
                else:
                    if node.val % 2 != 0: 
                        return False
                    if prev is not None and node.val >= prev:  
                        return False

                
                prev = node.val

                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            counter += 1  

        return True
