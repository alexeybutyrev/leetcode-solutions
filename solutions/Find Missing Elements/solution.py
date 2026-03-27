# Problem: Find Missing Elements
# Language: python3
# Runtime: 3 ms
# Memory: 17.9 MB

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn = min(nums)
        mx = max(nums)
        s = set(nums)
        ans = []
        for x in range(mn, mx + 1):
            if x not in s:
                ans.append(x)
        return ans