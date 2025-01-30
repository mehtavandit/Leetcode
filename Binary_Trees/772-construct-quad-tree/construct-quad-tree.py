"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        rows = len(grid)
        cols = len(grid[0])

        def is_all_same(grid):
            value = grid[0][0]
            for r in grid:
                for val in r:
                    if val!=value:
                        return False
            return True

        if is_all_same(grid):
            return Node(val=grid[0][0], isLeaf = True)

        midr = rows // 2
        midc = cols // 2

        topLeft = self.construct([row[:midc] for row in grid[:midr]])
        topRight = self.construct([row[midc:] for row in grid[:midr]])
        bottomLeft = self.construct([row[:midc] for row in grid[midr:]])
        bottomRight = self.construct([row[midc:] for row in grid[midr:]])

        return Node(val=False, isLeaf=False, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)
