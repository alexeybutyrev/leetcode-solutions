# Problem: Find First Palindromic String in the Array
# Language: python3
# Runtime: 71 ms
# Memory: 16.6 MB

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for x in words:
            if x == x[::-1]:
                return x
        return ""