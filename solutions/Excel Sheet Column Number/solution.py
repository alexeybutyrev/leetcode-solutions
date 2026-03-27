# Problem: Excel Sheet Column Number
# Language: python3
# Runtime: 32 ms
# Memory: 13.8 MB

class Solution:
    def titleToNumber(self, s: str) -> int:
        
        d = {}
        for l in range(ord('A'),ord('Z')+1,1):
            d[chr(l)] = l - ord('A') + 1
        
        n = len(s)
        
        sm = 0 
        for i in range(n):
            sm += (d[s[i]] * 26 ** (n - i-1))
        #sm += d[s[-1]]
        return sm