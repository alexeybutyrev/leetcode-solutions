# Problem: Paint House IV
# Language: python3
# Runtime: 2025 ms
# Memory: 139.7 MB

class Solution:
    def minCost(self, n: int, A: List[List[int]]) -> int:
        N = n // 2

        A1 = A[:N]
        A2 = A[N:][::-1]

        
        @cache
        def dp(i, a, b):
            if i == N: return 0

            ans = inf
            for x in range(0,3):
                for y in range(0,3):
                    if x != y and x != a and y != b:
                        ans = min(ans, A1[i][x] + A2[i][y] + dp(i+1, x, y))
            return ans
        
        return dp(0,-1,-1)
        
            
        
        return 1