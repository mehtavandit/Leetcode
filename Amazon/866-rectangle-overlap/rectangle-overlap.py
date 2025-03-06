class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        horizontal = False
        vertical = False
        # rec2.x1 < rec1.x2 and rec2.x2 > rec1.x1
        if rec2[0] < rec1[2] and rec2[2] > rec1[0]:
            horizontal = True
        # rec2.y1 < rec1.y2 and rec2.y2 > rec1.y1
        if rec2[1] < rec1[3] and rec2[3] > rec1[1]:
            vertical = True
        return horizontal and vertical