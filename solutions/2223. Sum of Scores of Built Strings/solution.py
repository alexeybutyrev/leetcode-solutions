# Problem: Sum of Scores of Built Strings
# Language: python3
# Runtime: 825 ms
# Memory: 18.8 MB

from sortedcontainers import SortedSet

class Trie:
    def __init__(self):
        self.t = defaultdict(Trie)
        self.iw = False

    def addWord(self, word: str) -> None:
        curr = self
        for l in word: curr = curr.t[l]
        curr.iw = True
        
    def search(self, word: str, curr = None) -> bool:
        
        if not curr: return self.search(word, self)
        ans = 0
        for l in word:
            if l in curr.t:
                ans += 1
                curr = curr.t[l]
            else:
                return ans
        return ans
        
    
    
class Solution:
    def sumScores(self, s: str) -> int:
        
        def z_function(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            return z
        
        return sum(z_function(s)) + len(s)
        
        