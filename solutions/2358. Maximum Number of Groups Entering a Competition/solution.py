# Problem: Maximum Number of Groups Entering a Competition
# Language: python3
# Runtime: 745 ms
# Memory: 27.3 MB

from itertools import accumulate
class Solution:
    def maximumGroups(self, A: List[int]) -> int:
        A.sort()
        
        c = 0
        s = 0
        
        cc = 0
        ss = 0
        ans = 0
        for a in A:
            c += 1
            s += a
            
            if c > cc and s > ss:
                ans += 1
                cc,ss = c,s
                c = 0
                s = 0
        return ans 
            
        