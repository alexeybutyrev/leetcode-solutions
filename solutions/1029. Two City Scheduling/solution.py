# Problem: Two City Scheduling
# Language: python3
# Runtime: 52 ms
# Memory: 13.8 MB

class Solution:
    def twoCitySchedCost(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x: x[0] - x[1])
        ans = 0
        for i in range((N:=len(A)//2)):
            ans += A[i][0] + A[i+N][1]
        return ans
