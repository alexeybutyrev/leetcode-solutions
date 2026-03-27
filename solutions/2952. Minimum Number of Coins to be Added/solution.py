# Problem: Minimum Number of Coins to be Added
# Language: python3
# Runtime: 598 ms
# Memory: 30.4 MB

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        A = sorted(coins) + [target + 1]
        
        b = 0
        ans = 0
        for x in A:
            while x > b + 1:
                b = 2 * b + 1
                ans += 1
            b += x
        return ans
            