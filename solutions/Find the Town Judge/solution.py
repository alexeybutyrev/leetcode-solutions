# Problem: Find the Town Judge
# Language: python3
# Runtime: 622 ms
# Memory: 21.7 MB

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inb = Counter()
        out = Counter()
        
        for u,v in trust:
            inb[u] += 1
            out[v] += 1
        
        for u in range(1,n+1):
            if inb[u] == 0 and out[u] == n -1:
                return u
        return -1