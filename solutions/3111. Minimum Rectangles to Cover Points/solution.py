# Problem: Minimum Rectangles to Cover Points
# Language: python3
# Runtime: 1003 ms
# Memory: 62.7 MB

class Solution:
    def minRectanglesToCoverPoints(self, A: List[List[int]], w: int) -> int:
        A.sort()
        
        ans = 1
        i = 0
        for j in range(1,len(A)):
            if A[j][0] - A[i][0] > w:
                ans += 1
                i = j
        return ans