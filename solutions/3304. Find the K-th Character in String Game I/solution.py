# Problem: Find the K-th Character in String Game I
# Language: python3
# Runtime: 45 ms
# Memory: 16.5 MB

class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'a'

        while len(s) < k:
            s0 = s
            for x in s:
                c = chr(ord(x) + 1)
                if c > 'z':
                    c = 'a'
                s0 += c
            s = s0
        return s[k-1]