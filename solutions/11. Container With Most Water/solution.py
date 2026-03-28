# Problem: Container With Most Water
# Language: python3
# Runtime: 720 ms
# Memory: 26.6 MB

class Solution:
    def maxArea(self, A: List[int]) -> int:
        N = len(A)
        i = 0
        j = N - 1
        
        S = min(A[i], A[j]) * (j - i)
        while i < j:
            if A[i] < A[j]:
                i += 1
            else:
                j -= 1
            
            S = max(S, min(A[i],A[j]) * (j-i))
        return S