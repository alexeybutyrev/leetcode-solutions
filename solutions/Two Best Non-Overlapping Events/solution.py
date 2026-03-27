# Problem: Two Best Non-Overlapping Events
# Language: python3
# Runtime: 1728 ms
# Memory: 57.7 MB

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        
        L = sorted(events, key = lambda x: x[0])
        R = sorted(events, key = lambda x: x[1])
        
        mx = [v for _,_,v in L]
        ans = max(mx)
        for i in range(N-2,-1,-1):
            mx[i] = max(mx[i],mx[i+1])
        i = 0
        for s,e,v in R:
            while i < N and e >= L[i][0]:
                i+=1
            
            if i < N:
                ans = max(ans, mx[i] + v)
            
        
        return ans