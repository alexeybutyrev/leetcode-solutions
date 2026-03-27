# Problem: Calculate Money in Leetcode Bank
# Language: python3
# Runtime: 0 ms
# Memory: 17.7 MB

class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        ans = w * 28 + w*(w-1)//2 * 7
        left = n % 7
        ans += (w + 1) * left + left * (left - 1) // 2
        return ans