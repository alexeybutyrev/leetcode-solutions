# Problem: Implement Trie II (Prefix Tree)
# Language: python3
# Runtime: 305 ms
# Memory: 30.2 MB

class Trie:

    def __init__(self):
        self.trie = defaultdict(Trie)
        self.count = 0

    def insert(self, word: str) -> None:
        curr = self
        for l in word:
            curr = curr.trie[l]
            curr.count += 1
        curr = curr.trie['$']
        curr.count += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self
        for l in word:
            if l not in curr.trie:
                return 0
            curr = curr.trie[l]
        if '$' not in curr.trie: return 0
        curr = curr.trie['$']
        return curr.count

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self
        for l in prefix:
            if l not in curr.trie:
                return 0
            curr = curr.trie[l]
        return curr.count

    def erase(self, word: str) -> None:
        curr = self
        for l in word:
            curr = curr.trie[l]
            curr.count -= 1
        curr = curr.trie['$']
        curr.count -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)