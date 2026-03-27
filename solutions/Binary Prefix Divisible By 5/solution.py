# Problem: Binary Prefix Divisible By 5
# Language: python3
# Runtime: 92 ms
# Memory: 19.1 MB

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x = 0
        ans = []
        for b in nums:
            x |= b
            
            ans.append(x % 5 == 0)
            x <<= 1
        return ans