# Problem: Two Best Non-Overlapping Events
# Language: python3
# Runtime: 2036 ms
# Memory: 56.7 MB

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        A = []
        B = []
        ans = 0
        for s,e,v in events:
            A.append((s,1,v))
            A.append((e+1,-1,v))
            ans = max(ans, v)
        A.sort()
        maxb = 0
        
        for x,t,v in A:
            if t == 1:
                ans = max(ans, v + maxb)
            else:
                maxb = max(maxb, v)
            
        return ans