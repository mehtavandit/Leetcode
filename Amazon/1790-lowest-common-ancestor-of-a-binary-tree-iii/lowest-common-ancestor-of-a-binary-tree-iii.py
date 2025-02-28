"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_depth = self.get_depth(p)
        q_depth = self.get_depth(q)
        
        while p_depth>q_depth:
            p = p.parent
            p_depth -= 1

        while q_depth > p_depth:
            q = q.parent
            q_depth -=1

        while p!=q:
            p = p.parent
            q = q.parent
        
        return p

    def get_depth(self, p):
        depth = 0
        while p:
            p = p.parent
            depth += 1
        return depth
