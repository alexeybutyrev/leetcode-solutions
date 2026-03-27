# Problem: Longest Consecutive Sequence
# Language: python3
# Runtime: 48 ms
# Memory: 15.5 MB

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        N = len(nums)
        s = set(nums)
        
        
        ln = 1
        while s:
            mn = min(s)
            l = 1
            while s and mn in s:
                s.remove(mn)
                if mn + 1 in s:
                    l += 1
                    mn += 1
                ln = max(ln, l)
            
            
            
        return ln
            
        