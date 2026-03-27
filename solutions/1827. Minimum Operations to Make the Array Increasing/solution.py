# Problem: Minimum Operations to Make the Array Increasing
# Language: python3
# Runtime: 136 ms
# Memory: 15.2 MB

class Solution:
    def minOperations(self, A: List[int]) -> int:
        
        count = 0
        for i in range(1, len(A)):
            if A[i] <= A[i-1]:
                count += A[i-1] + 1 - A[i]
                A[i] = A[i-1] + 1
        
        return count
        