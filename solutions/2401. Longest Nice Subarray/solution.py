# Problem: Longest Nice Subarray
# Language: python3
# Runtime: 836 ms
# Memory: 28.8 MB

class Solution:
    def longestNiceSubarray(self, A: List[int]) -> int:
        i = 0
        N = len(A)
        ans = 1
        
        x = A[i] 
        i = 0
        j = 1
        while i < N and j < N:
            while j < N and x & A[j] == 0:
                ans = max(ans, j - i + 1)
                x |= A[j]
                j += 1
                
            while j < N and i < N and x & A[j] != 0:
                x &= (~A[i])
                i += 1
            
            #j += 1
            
        return ans