# Problem: Reverse String
# Language: python
# Runtime: 168 ms
# Memory: 18.7 MB

class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1