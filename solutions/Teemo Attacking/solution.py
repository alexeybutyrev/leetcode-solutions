# Problem: Teemo Attacking
# Language: python3
# Runtime: 360 ms
# Memory: 15.4 MB

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        s = 0
        delta = 0
        n = len(timeSeries)
        t = timeSeries[0]
        for i in range(n):
            delta = timeSeries[i] - t
            if delta > 0:
                s+= duration
            else:
                s+= duration + delta
            t = timeSeries[i] + duration
            
        
        return s