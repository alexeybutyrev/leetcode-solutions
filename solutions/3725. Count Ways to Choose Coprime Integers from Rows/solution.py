# Problem: Count Ways to Choose Coprime Integers from Rows
# Language: python3
# Runtime: 3147 ms
# Memory: 27.7 MB

class Solution:
    def countCoprime(self, A: List[List[int]]) -> int:
        MOD = 10**9 + 7
        N,M = len(A), len(A[0])
        if N == 1: 
            return sum(1 if A[0][j] == 1 else 0 for j in range(M) )

        @cache
        def dp(i,x):
            if i == N - 1:
                ans = 0
                for j in range(M):
                    ans += int(gcd(A[i][j], x) == 1)
                    ans %= MOD
                return ans
            ans = 0
            left = N - i - 1
            for j in range(M):
                g = gcd(A[i][j], x)
                if g == 1:
                    ans += pow(M, left, MOD)
                    ans %= MOD
                else:
                    ans += dp(i+1,g)
                    ans %= MOD
            return ans

        ans = 0
        for j in range(M):
            if A[0][j] == 1:
                ans += pow(M, N-1, MOD)
                ans %= MOD
            else:
                ans += dp(1,A[0][j])
                ans %= MOD
        return ans