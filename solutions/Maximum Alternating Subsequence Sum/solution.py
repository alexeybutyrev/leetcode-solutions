# Problem: Maximum Alternating Subsequence Sum
# Language: python3
# Runtime: 1160 ms
# Memory: 28.5 MB

class Solution:
    def maxAlternatingSum(self, A: List[int]) -> int:
        
        odd = even = 0
        for x in A:
            ne = even
            even = max(even, odd - x)
            odd  = max(odd, ne + x)
        
        return max(even, odd)
            