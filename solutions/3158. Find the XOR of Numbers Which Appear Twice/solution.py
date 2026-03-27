# Problem: Find the XOR of Numbers Which Appear Twice
# Language: python3
# Runtime: 47 ms
# Memory: 16.5 MB

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c= Counter(nums)
        ans = 0
        for k,v in c.items():
            if v == 2:
                ans ^= k
        return ans