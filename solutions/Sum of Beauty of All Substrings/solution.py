# Problem: Sum of Beauty of All Substrings
# Language: python3
# Runtime: 3384 ms
# Memory: 14.3 MB

class Solution:
    def beautySum(self, S: str) -> int:
        N = len(S)
        ans = 0
        for i in range(N):
            c = Counter()
            MAX = -inf
            MIN = inf
            for j in range(i,N):
                c[S[j]] += 1
                if len(c) > 1:
                    MAX = max(c.values())
                    MIN = min(c.values())
                    ans += MAX - MIN
                
        
        return ans
        