# Problem: Find the Value of the Partition
# Language: python3
# Runtime: 492 ms
# Memory: 29.8 MB

class Solution:
    def findValueOfPartition(self, A: List[int]) -> int:
        A.sort()
        N = len(A)
        return min(A[i+1] - A[i] for i in range(len(A)-1))