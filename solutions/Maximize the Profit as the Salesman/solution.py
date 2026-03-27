# Problem: Maximize the Profit as the Salesman
# Language: python3
# Runtime: 1524 ms
# Memory: 72.5 MB

class Solution:
    def maximizeTheProfit(self, n: int, A: List[List[int]]) -> int:
        A.sort(key = lambda x: x[0])
        Y = [x for x,_,_ in A]
        N = len(A)
        @cache
        def dp(i):
            if i >= N: return 0
            
            ind = bisect_left(Y, A[i][1]+1)
            s1 = A[i][2] + dp(ind)
            s2 = dp(i+1)
            return max(s1,s2)
        
        return dp(0)