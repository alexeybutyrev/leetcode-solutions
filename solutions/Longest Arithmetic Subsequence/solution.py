# Problem: Longest Arithmetic Subsequence
# Language: python3
# Runtime: 4113 ms
# Memory: 254.4 MB

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        d = defaultdict(list)
        for i,x in enumerate(A):
            d[x].append(i)
        
        N = len(A)
        @cache
        def dp(i,dx):
            if i == N: return 0
            n = A[i] + dx
            if n in d:
                ind = bisect_left(d[n], i+1)
                if ind == len(d[n]): return 0
                return 1 + dp(d[n][ind],dx)
                
            else:
                return 0
        
        ans = 0
        N = len(A)
        for i in range(N):
            for j in range(i+1,N):
                dx = A[j] - A[i]
                ans = max(ans, 2 + dp(j,dx))
        
        return ans