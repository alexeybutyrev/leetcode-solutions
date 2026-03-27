# Problem: Add Digits
# Language: python3
# Runtime: 52 ms
# Memory: 16.2 MB

class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = int(sum(int(x) for x in str(num)))
        return int(num)