# Problem: Maximum Distance in Arrays
# Language: python3
# Runtime: 160 ms
# Memory: 16.9 MB

from heapq import *
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        lefts  = [(n[0],i)  for (i,n) in enumerate(arrays)]
        rights = [(n[-1],i) for (i,n) in enumerate(arrays)]
        
        lefts.sort()
        rights.sort(reverse = True)
        #print(lefts,rights)
        
        d = 0
        for i in range(len(lefts)):
            if lefts[0][1] != rights[i][1]:
                d = max(d, abs(lefts[0][0]-rights[i][0]))
                break
        
        for i in range(len(lefts)):
            if lefts[i][1] != rights[0][1]:
                d = max(d, abs(lefts[i][0]-rights[0][0]))
                break
        return d