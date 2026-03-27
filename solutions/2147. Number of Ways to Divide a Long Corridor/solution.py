# Problem: Number of Ways to Divide a Long Corridor
# Language: python3
# Runtime: 287 ms
# Memory: 22.5 MB

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        count = 0
        MOD = 10**9 + 7
        
        A = []
        for i,c in enumerate(corridor):
            if c == "S":
                A.append(i)
        
        N = len(A)
        
        if N % 2 == 1 or N < 2:
            return 0
        
        N = len(A)
        ans = 1
        for i in range(N // 2 - 1):
            ans *= (A[2 *i + 2] - A[2*i+1])
            ans %= MOD
        return ans
            