# Problem: Maximum Consecutive Floors Without Special Floors
# Language: python3
# Runtime: 911 ms
# Memory: 28 MB

class Solution:
    def maxConsecutive(self, bottom: int, top: int, A: List[int]) -> int:
        ans = 0
        A.sort()
        for i in range(1,len(A)):
            ans = max(ans, A[i] - A[i-1]-1)
        
        if bottom not in A:
            ans = max(ans, A[0] - bottom)
        if top not in A:
            ans = max(ans, top - A[-1])
        
        return ans
    