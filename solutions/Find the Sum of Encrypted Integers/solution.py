# Problem: Find the Sum of Encrypted Integers
# Language: python3
# Runtime: 49 ms
# Memory: 16.5 MB

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            d = list(str(x))
            ans += int(max(d) * len(d))
        return ans
            