# Problem: Difference Between Element Sum and Digit Sum of an Array
# Language: python3
# Runtime: 165 ms
# Memory: 14.1 MB

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = 0
        sa = 0
        for n in nums:
            s += n
            sa += sum([int(d) for d in str(n)])
        
        return abs(s-sa)