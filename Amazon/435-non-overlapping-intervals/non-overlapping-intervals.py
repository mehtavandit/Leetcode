class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        ans = 0
        end_time = float('-inf')
        
        for x, y in intervals:
            if x >= end_time:
                end_time = y
            else:
                ans += 1

        return ans