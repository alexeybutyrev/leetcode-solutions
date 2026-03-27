# Problem: Non-overlapping Intervals
# Language: python3
# Runtime: 68 ms
# Memory: 17.5 MB

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[1])
        N = len(intervals)
        res = []
        maxR = -inf
        count = 0
        for i in range(N):
            if intervals[i][0] >= maxR:
                count += 1
                maxR = max(intervals[i][1], maxR)
        
        return N - count