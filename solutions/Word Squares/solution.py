# Problem: Word Squares
# Language: python3
# Runtime: 356 ms
# Memory: 16.2 MB

class Trie:
    
    def __init__(self):
        self.children = {}
        self.ans = []
        self.N = 0 
    
    
    def add(self, word):
        if not self.children:
            self.children[""] = {}
        
        self.N = len(word)
        curr = self.children[""]
        if 'words' not in curr:
                curr['words'] = []
        curr['words'].append(word)
            
        for l in word:
            if 'words' not in curr:
                curr['words'] = []
            curr['words'].append(word)
            if l not in curr:
                curr[l] = {}
            curr = curr[l]
        
        if 'words' not in curr:
                curr['words'] = []
        curr['words'].append(word)
        
    def find_words(self, words):
        if len(words) == self.N:
            self.ans.append(words)
        else:
            curr = self.children[""]
            M = len(words)
            for i,w in enumerate(words):
                if w[M] in curr:
                    curr = curr[w[M]]
                else:
                    break
            else:
                for l in curr:
                    if l != 'words':
                        for tw in curr[l]['words']:
                            self.find_words(words + [tw])

    
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        T = Trie()
        
        for w in words:
            T.add(w)
        
        
        for w in words:
            T.find_words([w])
        
        return T.ans
        