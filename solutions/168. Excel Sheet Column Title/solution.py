# Problem: Excel Sheet Column Title
# Language: python3
# Runtime: 29 ms
# Memory: 16.3 MB

class Solution:
    def convertToTitle(self, x: int) -> str:
        ans = ""
        while x:
            c = (x -1) % 26
            ans = chr(ord('a') + c).upper() + ans
            x-=(c-1)
            x //= 26
        return ans