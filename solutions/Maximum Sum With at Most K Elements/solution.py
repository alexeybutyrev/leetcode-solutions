# Problem: Maximum Sum With at Most K Elements
# Language: python3
# Runtime: 323 ms
# Memory: 46.9 MB

class Solution:
    def maxSum(self, A: List[List[int]], limits: List[int], k: int) -> int:
        N, M = len(A), len(A[0])
        h = []
        for x in A:
            x.sort(reverse = True)
        
        for i in range(N):
            for j in range(limits[i]):
                heappush(h,-A[i][j])

        s = 0
        while h and k:
            s += -heappop(h)
            k -= 1
        return s