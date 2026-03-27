# Problem: Maximum Number of Events That Can Be Attended II
# Language: python3
# Runtime: 989 ms
# Memory: 213.3 MB

class Solution:
    def maxValue(self, A: List[List[int]], k: int) -> int:
        N = len(A)
        A.sort()
        graph = {}
        for i in range(N):
            for j in range(i+1,N):
                if A[j][0] > A[i][1]:
                    graph[i] = j
                    break
            else:
                graph[i] = N
        
        @cache
        def dp(i,k):
            if i == N or k == 0:
                return 0
            s1 = A[i][2] + dp(graph[i], k-1)
            s2 = dp(i+1, k)
        
            return max(s1,s2)
        
        return dp(0,k)
            