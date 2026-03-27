# Problem: Count Elements With Maximum Frequency
# Language: python3
# Runtime: 0 ms
# Memory: 17.6 MB

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums).values()
        mx = max(c)
        ans = 0
        for x in c:
            if x == mx:
                ans += mx
        return ans
        