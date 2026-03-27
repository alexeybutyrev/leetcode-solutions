# Problem: Meeting Rooms
# Language: python3
# Runtime: 64 ms
# Memory: 17.1 MB

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if not intervals:
            return True
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        
        return True