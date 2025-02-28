class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if len(intervals) <= 1:
            return True
            
        sorted_intervals = sorted(intervals, key = lambda x: x[1])

        end_time =  sorted_intervals[0][1]

        for i in range(1, len(sorted_intervals)):
            if  sorted_intervals[i][0] < end_time:
                return False
            end_time  =  sorted_intervals[i][1]

        return True