# Problem: Minimum Partition Score
# Language: python3
# Runtime: 13328 ms
# Memory: 19.9 MB

from collections import deque

class Solution:
    def minPartitionScore(self, A: List[int], K: int) -> int:
        N = len(A)
        F = [0] * (N + 1)
        for i in range(N):
            F[i+1] = F[i] + A[i]
            
        # dp[i] represents min score for prefix of length i
        dp = [0] * (N + 1)
        # Base case: k=1
        for i in range(1, N + 1):
            s = F[i]
            dp[i] = (s * (s + 1)) // 2
            
        # Iterating through remaining partitions
        for k in range(2, K + 1):
            new_dp = [0] * (N + 1)
            dq = deque()
            
            # Helper to get intersection x-coordinate of two lines
            # Line: y = mx + c -> m=-F[j], c=dp[j] + (F[j]^2 - F[j])/2
            def get_m_c(j):
                m = -F[j]
                c = dp[j] + (F[j] * F[j] - F[j]) // 2
                return m, c

            def intersect(j1, j2):
                m1, c1 = get_m_c(j1)
                m2, c2 = get_m_c(j2)
                return (c2 - c1) / (m1 - m2)

            # We can only start a k-th partition from index j >= k-1
            for i in range(1, N + 1):
                # Add line from previous DP state (j = i-1)
                j_new = i - 1
                while len(dq) >= 2 and intersect(dq[-2], dq[-1]) >= intersect(dq[-1], j_new):
                    dq.pop()
                dq.append(j_new)
                
                # Query: F[i] is our x. Remove lines that are no longer optimal
                while len(dq) >= 2 and intersect(dq[0], dq[1]) <= F[i]:
                    dq.popleft()
                
                best_j = dq[0]
                m, c = get_m_c(best_j)
                new_dp[i] = (F[i] * F[i] + F[i]) // 2 + (m * F[i] + c)
            
            dp = new_dp
            
        return dp[N]