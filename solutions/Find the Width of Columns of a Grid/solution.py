# Problem: Find the Width of Columns of a Grid
# Language: python3
# Runtime: 129 ms
# Memory: 15.4 MB

class Solution:
    def findColumnWidth(self, A: List[List[int]]) -> List[int]:
        ans = []
        for j in range(len(A[0])):
            x = 0
            for i in range(len(A)):
                x = max(x, len(str(A[i][j])))
            ans.append(x)
        return ans
            