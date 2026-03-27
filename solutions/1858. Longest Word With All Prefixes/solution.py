# Problem: Longest Word With All Prefixes
# Language: python3
# Runtime: 1470 ms
# Memory: 56.3 MB

class Node:
    def __init__(self):
        self.t = defaultdict(Node)
        self.isword = False
    
    def add(self, word):
        curr = self
        for l in word:
            curr = curr.t[l]
        curr.isword = True
    
    def get_count(self,word):
        curr = self
        for l in word:
            curr = curr.t[l]
            if not curr.isword:
                return False
        return True
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Node()
        for w in words:
            t.add(w)
        
        words.sort(key = lambda x: (-len(x),x))
        for w in words:
            if t.get_count(w):
                return w
        return ""