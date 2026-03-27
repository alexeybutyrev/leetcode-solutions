# Problem: Transform Array by Parity
# Language: python3
# Runtime: 0 ms
# Memory: 18.1 MB

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        o, e = 0, 0
        for x in nums:
            if x %2:
                o+=1
            else:
                e += 1
        return [0] * e + [1] * o