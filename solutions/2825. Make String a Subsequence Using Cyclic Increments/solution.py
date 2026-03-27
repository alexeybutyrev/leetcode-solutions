# Problem: Make String a Subsequence Using Cyclic Increments
# Language: python3
# Runtime: 293 ms
# Memory: 128.3 MB

class Solution:
    def canMakeSubsequence(self, A: str, B: str) -> bool:
        NA, NB = len(A), len(B)
        
        def move(i, j):
            
            if j == NB: return True
            if i == NA: return False

            
            if A[i] == B[j]: return move(i+1,j+1)
            
            
            
            if A[i] == 'z' and B[j] == 'a': return move(i+1,j+1)
            if ord(A[i]) == ord(B[j]) - 1: return move(i+1,j+1)
            
            return move(i+1, j)
        
        return move(0,0)
            
            