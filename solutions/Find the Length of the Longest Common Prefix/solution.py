# Problem: Find the Length of the Longest Common Prefix
# Language: python3
# Runtime: 1049 ms
# Memory: 44.3 MB

class WordDictionary:
    def __init__(self):
        self.t = defaultdict(WordDictionary)
        self.iw = False

    def add(self, word: str) -> None:
        curr = self
        for l in word: curr = curr.t[l]
        curr.iw = True
        
    def search(self, word):
        # check if we at the end
        curr = self
        for i,l in enumerate(word):
            if l in curr.t:
                curr = curr.t[l]
            else:
                return i
                
        return len(word)
        
        # check if we started
        
    
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        A = set(str(x) for x in arr1)
        B = set(str(x) for x in arr2)
        
        T = WordDictionary()
        for x in A:
            T.add(x)
        
        
        ans = 0
        for x in B:
            lans = T.search(x)
            ans = max(ans,lans)
        
        
        return ans
                
        