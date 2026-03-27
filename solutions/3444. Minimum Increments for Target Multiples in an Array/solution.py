# Problem: Minimum Increments for Target Multiples in an Array
# Language: python3
# Runtime: 6760 ms
# Memory: 342.7 MB

class Solution:
    def minimumIncrements(self, A: List[int], T: List[int]) -> int:
        
        N = len(A)
        M = len(T)

        @cache
        def dp(i,m):
            if i == N:
                return 0 if m == 0 else inf

            ans = dp(i+1,m)
            for x in range(1<<M):
                if x & m == x:
                    c = 1
                    for j in range(M):
                        if (x ^ m) & (1<<j):
                            c = lcm(c, T[j])
                    r = (c - A[i] % c) % c
                    ans = min(ans, r + dp(i+1,x))
            return ans

        return dp(0, (1<< M)-1)