# Problem: Missing Element in Sorted Array
# Language: python3
# Runtime: 556 ms
# Memory: 20.3 MB

# 4, 7, 9, 10
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        for i in range(n - 1):
            nm = nums[i+1] - nums[i] - 1
            
            if nm >= k:
                return nums[i] + k
            
            k -= nm
        
        return nums[n-1] + k