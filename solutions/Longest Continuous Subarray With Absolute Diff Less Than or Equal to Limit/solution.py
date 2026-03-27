# Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Language: python3
# Runtime: 672 ms
# Memory: 24 MB

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        n = len(nums)
        ln = 0
        count = 0
        if 1 == n:
            return 1
        
        for i in range(n-1):
            max_el = nums[i]
            min_el = nums[i]
            count = 1
            for j in range(i+1,n):
                max_el = max(max_el, nums[j])
                min_el = min(min_el, nums[j])
                
                if abs(max_el-min_el) <= limit:
                    count+=1
                    ln = max(ln, count)
                else:
                    break
            if j == n -1:
                return ln
        return ln
                