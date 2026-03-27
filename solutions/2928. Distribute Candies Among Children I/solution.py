# Problem: Distribute Candies Among Children I
# Language: python3
# Runtime: 626 ms
# Memory: 16.3 MB

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        ans = 0
        for x in range(min(n,limit) + 1):
            for y in range(min(n,limit) + 1):
                for z in range(min(n,limit) + 1):
                    if x + y + z == n:
                        ans += 1
        return ans
            