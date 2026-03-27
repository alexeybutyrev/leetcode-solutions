# Problem: Decrease Elements To Make Array Zigzag
# Language: python3
# Runtime: 32 ms
# Memory: 14.3 MB

class Solution:
    def movesToMakeZigzag(self, A: List[int]) -> int:
        N = len(A)
        A = [inf] + A + [inf]
        
        evens = sum( max(0, A[i] - min(A[i+1], A[i-1]) + 1) for i in range(1,N+1,2)   )
        odds  = sum( max(0, A[i] - min(A[i+1], A[i-1]) + 1) for i in range(2,N+1,2) )
        return min(evens, odds)