# Problem: Check If a Word Occurs As a Prefix of Any Word in a Sentence
# Language: python3
# Runtime: 64 ms
# Memory: 13.7 MB

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if not sentence:
            return -1
        
        words = sentence.split(" ")
        n = len(words)
        for i in range(n):
            if words[i].startswith(searchWord):
                return i + 1
        return -1