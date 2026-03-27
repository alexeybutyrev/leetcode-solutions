# Problem: Average Value of Even Numbers That Are Divisible by Three
# Language: python3
# Runtime: 200 ms
# Memory: 14.2 MB

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        c = 0
        s = 0
        for x in nums:
            if x % 6 == 0:
                c += 1
                s += x
        return floor(s/c) if c else 0
                