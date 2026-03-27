# Problem: Minimum Number of Operations to Make All Array Elements Equal to 1
# Language: python3
# Runtime: 107 ms
# Memory: 16.8 MB

class Solution:
    def minOperations(self, A: List[int]) -> int:
        N = len(A)
        @cache
        def dp(A):
            if sum(A) == N: return 0
            A = list(A)
            ans = inf
            for i in range(N-1):
                
                c = gcd(A[i],A[i+1])
                if c == 1:
                    s = 0
                    for x in A:
                        if x != 1:
                            s += 1
                    return s
                if A[i] != c:
                    x = A[i]
                    A[i] = c
                    ans = min(ans, 1 + dp(tuple(A)))
                    A[i] = x
                
                if A[i+1] != c:
                    x = A[i+1]
                    A[i+1] = c
                    ans = min(ans, 1 + dp(tuple(A)))
                    A[i+1] = x
            return ans
        
        ans = dp(tuple(A))
        
        return  -1  if inf == ans else ans
                