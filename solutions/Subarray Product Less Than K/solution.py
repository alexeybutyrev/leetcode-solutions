# Problem: Subarray Product Less Than K
# Language: python3
# Runtime: 1052 ms
# Memory: 18.3 MB

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        p = 1
        left = 0
        count = 0
        
        for right,val in enumerate(nums):
            p *= val
            while p >= k:
                p /= nums[left]
                left +=1
            count += right - left + 1
        return count