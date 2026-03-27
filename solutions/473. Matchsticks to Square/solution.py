# Problem: Matchsticks to Square
# Language: python3
# Runtime: 627 ms
# Memory: 27.9 MB

class Solution:
    def makesquare(self, A: List[int]) -> bool:
        S = sum(A)
        if S % 4 != 0:
            return False
        
        size = S // 4
        N = len(A)
        T = (1 << N) - 1
        @cache
        def dp(mask,a):
            if mask == T and a == 0:
                return True
            
            if a == 0:
                a = size
            for i in range(N):
                if mask & (1 << i) == 0 and A[i] <= a:
                    if dp(mask | (1<<i), a - A[i]):
                        return True
            return False
        
        return dp(0,size)
                    