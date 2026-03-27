# Problem: Find the Pivot Integer
# Language: python3
# Runtime: 574 ms
# Memory: 19.3 MB

class Solution:
    def pivotInteger(self, n: int) -> int:
        A = list(range(1,n+1))
        
        for i in range(n):
            if sum(A[:i+1]) == sum(A[i:]):
                return i+1
        return -1