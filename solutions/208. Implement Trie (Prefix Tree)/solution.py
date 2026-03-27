# Problem: Implement Trie (Prefix Tree)
# Language: python3
# Runtime: 281 ms
# Memory: 27.7 MB

class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for l in word:
            if l not in curr:
                curr[l] = {}
            curr = curr[l]
        curr['$'] = {}
        
            
            

    def search(self, word: str) -> bool:
        curr = self.trie
        for l in word:
            if l not in curr:
                return False
            curr = curr[l]
        return "$" in curr
    

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for l in prefix:
            if l not in curr:
                return False
            curr = curr[l]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)