# Problem: Maximize the Topmost Element After K Moves
# Language: python3
# Runtime: 592 ms
# Memory: 27.9 MB

class Solution:
    def maximumTop(self, A: List[int], k: int) -> int:
        N = len(A)
        
        if k == 0:
            return A[0]
        
        if N == 1:
            return -1 if k & 1 else A[0]
        
        if k > N:
            return max(A)
        
        
        if k == 1:
            return A[1]

        if k == N:
            return max(A[:k-1])
        
        return max(max(A[:k-1]), A[k])
        