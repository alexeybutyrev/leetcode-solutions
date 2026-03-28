# Problem: Find the Highest Altitude
# Language: python3
# Runtime: 60 ms
# Memory: 14.3 MB

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        res = [0]
        
        for g in gain:
            res.append(res[-1] + g)
        
        return max(res)