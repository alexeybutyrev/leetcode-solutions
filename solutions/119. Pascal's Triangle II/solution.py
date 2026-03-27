# Problem: Pascal's Triangle II
# Language: python3
# Runtime: 30 ms
# Memory: 16.3 MB

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        A = [1]
        for _ in range(rowIndex):
            B = [1]
            for i in range(1,len(A)):
                B.append(A[i-1] + A[i])
            B.append(1)
            A = B[:]
        return A