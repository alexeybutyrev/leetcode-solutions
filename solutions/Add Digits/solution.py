# Problem: Add Digits
# Language: python3
# Runtime: 32 ms
# Memory: 13.8 MB

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: 
            return 0;
        if num % 9 == 0: 
            return 9;
        return num % 9