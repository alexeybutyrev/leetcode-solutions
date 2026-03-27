# Problem: Maximum Average Pass Ratio
# Language: python3
# Runtime: 4016 ms
# Memory: 64.1 MB

from heapq import *
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        A = [ ]
        for i, (p, s) in enumerate(classes):
            heappush(A, ( -(p + 1) / (s + 1) + p / s, p, s ) )
        
        
        
        for i in range(extraStudents):   
            gain, p, s = heappop(A)
            p += 1
            s += 1
            heappush( A, ( -(p + 1) / (s + 1) + p / s, p, s ))
         
        N = len(A)
        S0 = 0
        for _, p, s in A:
            S0 += p * 1.0 / s
        
        return S0 / N