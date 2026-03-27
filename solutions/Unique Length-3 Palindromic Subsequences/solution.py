# Problem: Unique Length-3 Palindromic Subsequences
# Language: python3
# Runtime: 467 ms
# Memory: 49 MB

from string import ascii_lowercase
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        c = Counter()
        A = []
        first = {}
        last  = {}
        curr = [0] * 26
        ch = lambda x: ord(x) - ord('a')
        for i,l in enumerate(s):
            if l not in first:
                first[l] = i
            last[l] = i
            curr[ch(l)] += 1
            A.append(curr[:])
        
        
        ans = 0
        seen = set()
        for c in ascii_lowercase:
            l = s.find(c)
            r = s.rfind(c)
            if l != r:
                d = [y - x for x,y in zip(A[l], A[r])]
                d[ch(c)] -= 1
                ans += sum( x>0 for x in d) 
        return ans