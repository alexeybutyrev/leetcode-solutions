# Problem: Consecutive Numbers Sum
# Language: python3
# Runtime: 254 ms
# Memory: 13.9 MB

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # n = (x + 1) + (x + 2) + ... (x + k) 
        # n = c * x + 1 + 2 + ..
        
        x = 1
        ans = 0
        while x * (x + 1) // 2 <= n:
            s = x * (x + 1) // 2
            if (n - s) % x == 0 and n - s >= 0:
                ans += 1
            x += 1
            
        return ans
        