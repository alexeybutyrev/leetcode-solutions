# Problem: Number of Ways to Paint N × 3 Grid
# Language: python3
# Runtime: 60 ms
# Memory: 14.5 MB

class Solution:
    def numOfWays(self, n: int) -> int:
        
        MOD = 10**9 + 7
        a121, a123 = 6,6
        
        for i in range(n-1):
            a121, a123 = 3 * a121 + 2 * a123, 2 * a121 + 2 * a123
        
        return  ( a121 + a123 ) % MOD
        