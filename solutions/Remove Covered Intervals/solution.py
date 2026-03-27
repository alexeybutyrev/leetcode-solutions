# Problem: Remove Covered Intervals
# Language: python3
# Runtime: 92 ms
# Memory: 14.4 MB

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        
        n = len(intervals)
        ind = 0
        lb, rb = intervals[ind][0], intervals[ind][1]
        count = 0 
        while ind < n:
            if lb == intervals[ind][0]:
                while ind < n and lb == intervals[ind][0]:
                    rb = max(rb, intervals[ind][1])
                    ind += 1
                count+=1
                continue
        
            if rb >= intervals[ind][1]:
                while ind < n and rb >= intervals[ind][1]:
                    ind += 1
            if ind < n:
                lb, rb = intervals[ind][0], intervals[ind][1]
                    
        
        return count
                
            
            
                
                
        