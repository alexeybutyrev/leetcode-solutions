# Problem: Points That Intersect With Cars
# Language: python3
# Runtime: 91 ms
# Memory: 16.2 MB

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        s = set()
        for x,y in nums:
            for i in range(x,y+1):
                s.add(i)
        return len(s)
            