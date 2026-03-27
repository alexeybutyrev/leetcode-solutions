# Problem: Length of Longest Fibonacci Subsequence
# Language: python3
# Runtime: 4242 ms
# Memory: 95.4 MB

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        N = len(A)
        DP = [[-1] * (N + 1) for _ in range(N+1)]

        def dp(i,j):

            if DP[i][j] == -1:
                s = A[i] + A[j]
                ans = 0
                k = bisect_right(A,s)
                k-=1
                if k < N and A[k] == s:
                    ans = max(ans, 1 + dp(j,k))
                DP[i][j] = ans
            return DP[i][j]
        
        ans = 2
        for i in range(N):
            for j in range(i+1,N):
                ans = max(ans, 2 + dp(i,j))
        return 0 if 2 == ans else ans