# Problem: Search Suggestions System
# Language: python3
# Runtime: 356 ms
# Memory: 22.7 MB

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.words = set()
    def add(self, word):
        curr = self
        curr.words.add(word)
        for l in word:
            curr = curr.children[l]
            curr.words.add(word)
    def search(self, word):
        ans = [[]] * len(word)
        curr = self
        for i,l in enumerate(word):
            if l in curr.children:
                curr = curr.children[l]
                ans[i] = sorted(curr.words)[0:3]
            else:
                return ans
        return ans
        
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Node()
        for p in products:
            t.add(p)
        
        return t.search(searchWord)
    