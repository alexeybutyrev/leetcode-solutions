# Problem: Find Polygon With the Largest Perimeter
# Language: python3
# Runtime: 499 ms
# Memory: 31.5 MB

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        s = 0
        ans = -1
        prev = 0
        for x in A:
            if x < s:
                ans = s + x
            
            s += x
        return ans
    
            
            