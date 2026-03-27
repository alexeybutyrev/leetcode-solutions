# Problem: Separate the Digits in an Array
# Language: python3
# Runtime: 80 ms
# Memory: 14.5 MB

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            for d in str(x):
                ans.append(int(d))
        return ans