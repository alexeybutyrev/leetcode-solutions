# Problem: Sum of Elements With Frequency Divisible by K
# Language: python3
# Runtime: 0 ms
# Memory: 17.9 MB

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        ans = 0
        c = Counter(nums)

        for x in c:
            if c[x] %k == 0:
                ans += c[x] * x
        return ans