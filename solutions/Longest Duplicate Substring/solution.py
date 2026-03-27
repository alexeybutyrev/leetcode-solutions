# Problem: Longest Duplicate Substring
# Language: python3
# Runtime: 1204 ms
# Memory: 19.7 MB

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        N = len(S)
        MOD = mod= 26**63 - 1
        A = [ord(a) - ord('a') for a in S]
        
        def map_word(K):
            p = pow(26,K,MOD)
            
            s = 0
            #s = reduce(lambda x, y: (x * 26 + y) % mod, A[:K], 0)
            for i in range(K):
                s = s * 26 + A[i]
                s %= MOD
            seen = {s}
            for i in range(K,N):
                s = (s*26 - A[i-K] * p + A[i])%MOD
                if s in seen: return i - K + 1
                seen.add(s)
            
        
        
        res = 0
        lo = 0
        hi = len(S)
    
        while lo < hi:
            mid = (lo + hi + 1) // 2
            p = map_word(mid)
            if p:
                lo = mid
                res = p
            else:
                hi = mid - 1
        
        return S[res:res+lo]
        