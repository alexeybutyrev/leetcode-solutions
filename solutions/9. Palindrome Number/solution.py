# Problem: Palindrome Number
# Language: python3
# Runtime: 44 ms
# Memory: 14.2 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]