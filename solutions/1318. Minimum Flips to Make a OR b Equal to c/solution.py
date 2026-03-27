# Problem: Minimum Flips to Make a OR b Equal to c
# Language: python3
# Runtime: 28 ms
# Memory: 14.4 MB

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        c = (a | b) ^ c
        
        count = 0
        i = 0
        while c:
            i += 1
            if (c >> 0) & 1:
                
                count += max(1,((a >> 0) & 1) + ((b >> 0) & 1))
            c >>=1
            a >>=1
            b >>=1
        return count