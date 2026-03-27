# Problem: Water Bottles
# Language: python3
# Runtime: 34 ms
# Memory: 16.3 MB

class Solution:
    def numWaterBottles(self, B: int, E: int) -> int:
        ans = 0
        while B >= E:
            k = B // E
            ans += E * k
            B -= E * k
            B += k
            
        return ans + B