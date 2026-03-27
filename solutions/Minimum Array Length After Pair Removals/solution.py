# Problem: Minimum Array Length After Pair Removals
# Language: python3
# Runtime: 1725 ms
# Memory: 31.2 MB

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        a = max(c.values())
        b = len(nums) - a
        ans = max(0,a - b)
        if ans == 0 and len(nums) & 1:
            return 1
        return ans