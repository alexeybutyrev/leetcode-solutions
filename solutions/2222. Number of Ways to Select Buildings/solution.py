# Problem: Number of Ways to Select Buildings
# Language: python3
# Runtime: 442 ms
# Memory: 15 MB

class Solution:
    def numberOfWays(self, s: str) -> int:
        
        z = o = oz = zo = 0
        ans = 0
        
        for l in s:
            if l == "0":
                z += 1
                oz += o
                ans += zo
            else:
                o += 1
                zo += z
                ans += oz
            
        return ans