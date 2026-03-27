# Problem: Count Submatrices with Top-Left Element and Sum Less Than k
# Language: python3
# Runtime: 171 ms
# Memory: 107.4 MB

class Solution:
    def countSubmatrices(self, A: List[List[int]], k: int) -> int:
        # accumulate
        for i,x in enumerate(A):
            A[i] = list(accumulate(x))
        # transpose
        A = list(zip(*A))
        # accumulate
        for i,x in enumerate(A):
            A[i] = list(accumulate(x))
        
        return sum([val <= k for row in A for val in row])