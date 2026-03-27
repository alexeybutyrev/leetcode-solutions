# Problem: Maximum Total Subarray Value I
# Language: python3
# Runtime: 12 ms
# Memory: 23.7 MB

class Solution:
    def maxTotalValue(self, A: List[int], k: int) -> int:

        ans = 0
        
        return (max(A) - min(A)) * k