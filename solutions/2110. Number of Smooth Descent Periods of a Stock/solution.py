# Problem: Number of Smooth Descent Periods of a Stock
# Language: python3
# Runtime: 55 ms
# Memory: 30.1 MB

class Solution:
    def getDescentPeriods(self, A: List[int]) -> int:
        q = []
        ans = 0
        for x in A:
            if not q or q[-1] - x == 1:
                q.append(x)
            else:
                ans += len(q) * (len(q) + 1) >> 1
                q = [x]
        
        return ans + (len(q) * (len(q) + 1) >> 1)
