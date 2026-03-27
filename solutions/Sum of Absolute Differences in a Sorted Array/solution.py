# Problem: Sum of Absolute Differences in a Sorted Array
# Language: python3
# Runtime: 708 ms
# Memory: 31.8 MB

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        S = sum(nums)
        N = len(nums)
        ans = []
        sl = 0
        for i,x in enumerate(nums):
            curr = i * x - sl
            curr += S-sl - (N - i) * x
            ans.append(curr)
            sl += x
        return ans