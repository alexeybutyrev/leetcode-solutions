# Problem: Find the Count of Monotonic Pairs I
# Language: python3
# Runtime: 2827 ms
# Memory: 115.8 MB

class Solution:
    def countOfPairs(self, A: List[int]) -> int:
        N = len(A)
        MOD = 10**9 + 7
        @cache
        def dp(i, x):
            if i == N: return 1
            Yb = A[i-1] - x
            Xb = x
            ans = 0
            for d in range(A[i]+1):
                Ya = A[i] - d
                Xa = d
                if Ya <= Yb and Xa >= Xb:
                    ans += dp(i+1,Xa)
                    ans %= MOD
            return ans
                    

        s = 0
        for x in range(A[0]+1):
            s += dp(1,x)
            s %= MOD

        return s