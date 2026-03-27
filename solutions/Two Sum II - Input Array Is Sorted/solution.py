# Problem: Two Sum II - Input Array Is Sorted
# Language: python3
# Runtime: 175 ms
# Memory: 14.8 MB

class Solution:
    def twoSum(self, A: List[int], target: int) -> List[int]:
        
        N = len(A)
        i = 0 
        j = N-1
        while i < N and j < N:
            if A[i] + A[j] == target:
                return [i+1,j+1]
            
            if A[i] + A[j] < target:
                i += 1
            else:
                j -=1
                
        
        return [-1,-1]
            