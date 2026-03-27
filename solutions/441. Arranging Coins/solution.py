# Problem: Arranging Coins
# Language: python3
# Runtime: 28 ms
# Memory: 13.9 MB

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        i = 0
        if n == 1:
            return 1
        while left + 1 != right:
            mid = (left + right) // 2
            v = mid * (mid + 1) 
            if v == 2 * n:
                return mid
            if v <= 2 * n:
                left = mid
            else:
                right = mid
            
        return left