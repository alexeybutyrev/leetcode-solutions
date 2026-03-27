# Problem: Maximum Earnings From Taxi
# Language: python3
# Runtime: 1856 ms
# Memory: 69.2 MB

class Solution:
    def maxTaxiEarnings(self, n: int, A: List[List[int]]) -> int:
        A.sort()
        N = len(A)
        D = [-1] * N
        X = [a[0] for a in A]
        @cache
        def dp(i):
            if i >= N:
                return 0
            
            s1 = dp(i+1)
            s2 = 0
            end = A[i][1]
            ind = bisect.bisect_left(X, end)
            s2 = A[i][2] + A[i][1] - A[i][0] + dp(ind)
            return max(s1,s2)
        
        return dp(0)
                    