# Problem: Count Prefix and Suffix Pairs II
# Language: python3
# Runtime: 1430 ms
# Memory: 224 MB

class Node:
    def __init__(self):
        self.t = defaultdict(Node)
        self.count = 0
        self.iw = False

    def add(self, word: str) -> None:
        curr = self
        
        for x,y in zip(word,word[::-1]):            
            curr = curr.t[(x,y)]
            curr.count += 1
            
        curr.iw = True
        return curr.count-1
        
    
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        T = Node()
        while words:
            w = words.pop()
            count = T.add(w)
            ans += count
            
        return ans