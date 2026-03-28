# Problem: Unique Length-3 Palindromic Subsequences
# Language: python3
# Runtime: 3260 ms
# Memory: 15 MB

class Solution:
    
    def __init__(self):
        self.s = set()
        for i in range(0,26):
            l = chr(i + ord('a'))
            for j in range(0,26):
                l2 = chr(j + ord('a'))
                self.s.add(l + l2 + l)
        
    def countPalindromicSubsequence(self, s: str) -> int:
        
        for j in range(0,26):
            l2 = chr(j + ord('a'))
        
        P = {}
        S = {}
        for i,l in enumerate(s):
            if l not in P:
                P[l] = i
            S[l] = i
        
        letters = {}
        for l in P:
            if P[l] != S[l]:
                letters[l] = (P[l],S[l])
        
        
        if not letters:
            return 0
        
        ans = set()
        for l,(start,end) in letters.items():
            for i in range(start+1, end):
                ans.add(l + s[i] + l)
        return len(ans)
            
                
        
        