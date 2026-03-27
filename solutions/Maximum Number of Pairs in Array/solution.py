# Problem: Maximum Number of Pairs in Array
# Language: python3
# Runtime: 49 ms
# Memory: 13.9 MB

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        
        c1 = 0
        c2 = 0
        for v in c.values():
            d,m = divmod(v,2)
            c1 += d
            c2 += m
        return [c1,c2]