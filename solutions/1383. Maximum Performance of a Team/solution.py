# Problem: Maximum Performance of a Team
# Language: python3
# Runtime: 404 ms
# Memory: 34 MB

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        A = list(zip(speed, efficiency))
        A.sort(key = lambda x: -x[1])
        
        h = []
        ss, p = 0,0
        for s,e in A:
            
            if len(h) > k - 1:
                ss -= heappop(h)
            
            heappush(h, s)
            ss += s
            p = max(p, ss * e)
        
        return p % MOD