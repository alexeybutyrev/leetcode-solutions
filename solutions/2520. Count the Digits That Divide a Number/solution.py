# Problem: Count the Digits That Divide a Number
# Language: python3
# Runtime: 36 ms
# Memory: 13.9 MB

class Solution:
    def countDigits(self, num: int) -> int:
        return sum(num % int(d) == 0 for d in str(num))