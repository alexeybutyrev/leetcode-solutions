# Problem: Design Add and Search Words Data Structure
# Language: python3
# Runtime: 256 ms
# Memory: 25.9 MB

class Node:
    def __init__(self):
        self.t = {}
    
    def add_word(self, word):
        curr = self.t
        for l in word:
            if l not in curr:
                curr[l] = {}
            curr = curr[l]
        curr["$"] = {}
        

def search_word(word: str, i = 0, curr= None) -> bool:
    if i == len(word):
        return "$" in curr
    letter = word[i]

    if letter == ".":
        for l in curr:
            if search_word(word, i + 1, curr[l]):
                return True

    if letter in curr: return search_word(word, i + 1, curr[letter])
    return False

class WordDictionary:
    def __init__(self):
        self.t = Node()

    def addWord(self, word: str) -> None:
        self.t.add_word(word)
        
    def search(self, word: str) -> bool:
        return search_word(word, 0, self.t.t)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)