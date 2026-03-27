# Problem: Sort Colors
# Language: python3
# Runtime: 24 ms
# Memory: 14.4 MB

class Solution:
    def sortColors(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(A)
        curr = p0 = 0
        p2 = N - 1
        
        while curr <= p2:
            if A[curr] == 0:
                A[curr], A[p0] = A[p0], A[curr]
                p0 += 1
                curr += 1
                
            elif A[curr] == 2:
                A[curr], A[p2] = A[p2],A[curr]
                p2 -= 1
            else:
                curr += 1
        
        return A