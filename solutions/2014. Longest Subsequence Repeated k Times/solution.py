# Problem: Longest Subsequence Repeated k Times
# Language: python3
# Runtime: 4237 ms
# Memory: 16.8 MB

class Solution:
    def longestSubsequenceRepeatedK(self, S: str, K: int) -> str:
        def isSubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)
    
        keys = "".join( k * (v // K) for k,v in Counter(S).items())
        
        
        combs = set()
        
        for l in range(len(keys) + 1):
            for cand in combinations(keys,l):
                for p in permutations(cand):
                    combs.add("".join(p))
        
        for c in sorted(combs, key = lambda x: (len(x), x), reverse = True):
            if isSubsequence(c * K,S):
                return c
        
                
        
                
    