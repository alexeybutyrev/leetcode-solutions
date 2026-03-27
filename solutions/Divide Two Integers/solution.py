# Problem: Divide Two Integers
# Language: python3
# Runtime: 36 ms
# Memory: 14.3 MB

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = int((str(dividend / divisor)).split(".")[0])
        if ans < 0:
            return ans if ans > -2**31 else -2**31
        
        if ans > 0:
            return ans if ans < 2**31 - 1 else 2**31 -1
        
        return ans
        
            