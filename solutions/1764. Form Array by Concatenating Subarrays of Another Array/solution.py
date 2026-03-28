# Problem: Form Array by Concatenating Subarrays of Another Array
# Language: python3
# Runtime: 976 ms
# Memory: 15.7 MB

class Solution:
    def canChoose(self, groups: List[List[int]], A: List[int]) -> bool:

        N = len(groups)
        def dp(i, j):
            if i == N:
                return True
            if j >= len(A):
                return False
            
            if dp(i,j+1):
                return True
            
            k = len(groups[i])
            if k + j <= len(A) and all(A[l+j] == x for l,x in enumerate(groups[i])):
                return dp(i+1, k + j)
            
            return False
        
        return dp(0,0)