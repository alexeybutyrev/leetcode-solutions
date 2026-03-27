# Problem: Maximum 69 Number
# Language: python3
# Runtime: 46 ms
# Memory: 13.9 MB

class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                return int("".join(s))
        return num