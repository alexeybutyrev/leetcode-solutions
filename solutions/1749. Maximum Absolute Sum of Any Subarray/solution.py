# Problem: Maximum Absolute Sum of Any Subarray
# Language: python3
# Runtime: 110 ms
# Memory: 29.4 MB

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def kadeine(A):
            curr = A[0]
            ans = A[0]

            for x in A[1:]:
                curr = max(curr+x, x)
                ans = max(ans, curr)
            return ans
        
        return max(kadeine(nums),kadeine([-x for x in nums]))