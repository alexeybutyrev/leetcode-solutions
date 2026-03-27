# Problem: Count Number of Distinct Integers After Reverse Operations
# Language: python3
# Runtime: 1928 ms
# Memory: 39.6 MB

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set()
        for a in nums:
            s.add(a)
            s.add(int(str(a)[::-1]))
        return len(s)