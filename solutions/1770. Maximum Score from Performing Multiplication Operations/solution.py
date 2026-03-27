# Problem: Maximum Score from Performing Multiplication Operations
# Language: python3
# Runtime: 9771 ms
# Memory: 32.5 MB

class Solution:
    def maximumScore(self, A: List[int], M: List[int]) -> int:
        K = len(M)
        N = len(A)
        
        @lru_cache(2000)
        def dp(i,j):
            k = i + j
            if k == K:
                return 0
            
            s1 = A[i] * M[k] + dp(i + 1, j)
            s2 = A[N - 1 - j] * M[k] + dp(i, j + 1)
            
            return max(s1, s2)
        
        ans = dp(0,0)
        #dp.cache_clear()
        return ans