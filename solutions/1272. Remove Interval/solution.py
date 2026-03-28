# Problem: Remove Interval
# Language: python3
# Runtime: 376 ms
# Memory: 19.8 MB

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        res = []
        n = len(intervals)
        
        i = 0
        while i < n and intervals[i][1] < toBeRemoved[0]:
            res.append(intervals[i])
            i+=1

            
        if i < n and intervals[i][1] > toBeRemoved[0] and intervals[i][0] < toBeRemoved[0]:
            res.append([intervals[i][0], toBeRemoved[0]])
        
        i = n - 1
        res2 = []
        while i >= 0 and intervals[i][0] > toBeRemoved[1]:
            res2.append(intervals[i])
            i-=1
        
        if i >= 0 and intervals[i][1] > toBeRemoved[1] and intervals[i][0] < toBeRemoved[1]:
            res2.append([toBeRemoved[1], intervals[i][1]])
        
        if res2:
            res2.reverse()
            res = res + res2
            
        return res
        