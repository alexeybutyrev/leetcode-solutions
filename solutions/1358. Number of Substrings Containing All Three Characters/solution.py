# Problem: Number of Substrings Containing All Three Characters
# Language: python3
# Runtime: 78 ms
# Memory: 17.9 MB

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = b= c = 0
        start = 0
        N = len(s)
        ans = 0
        for i,x in enumerate(s):
            if x == 'a': a += 1
            if x == 'b': b += 1
            if x == 'c': c += 1
            while a and b and c:
                ans += (N - i)
                
                x = s[start]
                if x == 'a': a -= 1
                if x == 'b': b -= 1
                if x == 'c': c -= 1
                start += 1
                
        return ans