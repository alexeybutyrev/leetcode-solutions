# Problem: Remove Digit From Number to Maximize Result
# Language: python3
# Runtime: 30 ms
# Memory: 13.8 MB

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = '0'
        for i,l in enumerate(number):
            if l == digit:
                ans = max(ans, number[:i] + number[i+1:])
        return ans