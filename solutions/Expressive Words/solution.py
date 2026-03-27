# Problem: Expressive Words
# Language: python3
# Runtime: 56 ms
# Memory: 14.5 MB

class Trie():
    def __init__(self):
        self.children = dict()
        self.count = 0
        self.ans = set()
    def add(self, w):
        if not self.children:
            self.children[""] = dict()
            
        trie = self.children[""]
        for l in w:
            if l not in trie:
                trie[l] = dict()
            trie = trie[l]
        
        
        trie["$"] = self.count
        self.count += 1
    
    def search(self, i, w, trie):
        if not trie:
            return 0
        N = len(w)
        
        if '$' in trie:
            if i == N:
                self.ans.add(trie['$'])
            
            if len(set(w[i:])) == 1 and i > 0 and w[i] == w[i-1] and N - i >= 2:
                self.ans.add(trie['$'])
        
        
        if i < N and w[i] in trie:
            self.search(i+1, w, trie[w[i]])
        
        if i > 0 and i < N and w[i-1] == w[i]:
            j = i
            while j < len(w) and w[j] == w[i-1]:
                j += 1
            if j < N and j - i >= 2:
                s = self.search(j, w, trie)
            else:
                s = 0

from itertools import groupby
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        if not S:
            return 0
        def groups(w):
            l = [( k, len(list(gi))) for k, gi in groupby(w)]
            return zip(*l)

        letters, counts = groups(S)
        ans = 0
        for word in words:
            wls, wcs = groups(word)
            if wls != letters: continue
                
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(counts, wcs))

        return ans