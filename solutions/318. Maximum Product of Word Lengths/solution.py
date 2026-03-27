# Problem: Maximum Product of Word Lengths
# Language: python3
# Runtime: 196 ms
# Memory: 14.6 MB

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        hm = Counter()
        for w in words:
            s = 0
            for l in set(w):
                s |= 1 << (ord(l) - ord('a'))
            hm[s] = max(hm[s], len(w))
        
        
        
        for x in hm:
            for y in hm:
                if x & y == 0:
                    ans = max(ans, hm[x] * hm[y])
        
        return ans