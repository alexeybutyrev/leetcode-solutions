# Problem: Partition String Into Minimum Beautiful Substrings
# Language: python3
# Runtime: 55 ms
# Memory: 16.5 MB

A = []

for i in range(8):
    A.append(bin(5 ** i)[2:])

class Solution:
    def minimumBeautifulSubstrings(self, S: str) -> int:

        N = len(S)
        @cache
        def dp(i):
            if i == N: return 0
            ans = inf
            for x in A:
                if S[i:].startswith(x):
                    ans = min(ans, 1 + dp(i + len(x)))
            
            
            return ans
        
        ans = dp(0)
        return -1 if ans == inf else ans
            