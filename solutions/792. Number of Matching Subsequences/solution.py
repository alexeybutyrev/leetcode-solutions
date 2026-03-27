# Problem: Number of Matching Subsequences
# Language: python3
# Runtime: 551 ms
# Memory: 15.6 MB

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isin(s,t):
            t = iter(t)
            
            return all(l in t for l in s)
        
        ans = 0
        hm = {}
        for w in words:
            if w not in hm:
                hm[w] = +(isin(w,s))
            ans += hm[w]
        return ans