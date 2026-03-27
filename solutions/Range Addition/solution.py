# Problem: Range Addition
# Language: python3
# Runtime: 168 ms
# Memory: 22.8 MB

class Solution:
    def getModifiedArray(self, N: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * (N + 1)
        for s, e, val in updates:
            ans[s] += val
            ans[e+1] -= val
        
        curr = 0
        for i in range(N):
            curr += ans[i]
            ans[i] = curr
            
        ans.pop()
        return ans