# Problem: Count Prefix and Suffix Pairs I
# Language: python3
# Runtime: 14 ms
# Memory: 18.1 MB

class WordDictionary:
    def __init__(self):
        self.t = defaultdict(WordDictionary)
        self.count = 0
        self.s = set()
        self.iw = False

    def add(self, word: str, ind: int) -> None:
        curr = self
        for l in word: 
            curr = curr.t[l]
            curr.count += 1
            curr.s.add(ind)
        curr.iw = True
        return curr.s
        
    
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        T = WordDictionary()
        RT = WordDictionary()
        ind = 0
        while words:
            ind += 1
            w = words.pop()
            c1 = T.add(w, ind)
            c2 = RT.add(w[::-1],ind)
            
            ans += len(c1 & c2) - 1
            
        return ans