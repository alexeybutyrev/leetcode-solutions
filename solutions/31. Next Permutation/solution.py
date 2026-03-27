# Problem: Next Permutation
# Language: python3
# Runtime: 44 ms
# Memory: 14.1 MB

class Solution:
    def nextPermutation(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(A)
        
        # find first drop
        
        for i in range(N-2,-1,-1):
            if A[i] < A[i+1]:
                break
        else:
            A.reverse()
            return A
        
        for j in range(i+1, N):
            if A[j] <= A[i]:
                A[i],A[j-1] = A[j-1],A[i]
                A[i+1:] = A[i+1:][::-1]
                return A
        
        A[i],A[j] = A[j],A[i]
        A[i+1:] = A[i+1:][::-1]
        return A
        
        
            