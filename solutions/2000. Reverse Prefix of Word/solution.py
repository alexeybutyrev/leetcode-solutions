# Problem: Reverse Prefix of Word
# Language: python3
# Runtime: 26 ms
# Memory: 16.7 MB

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i=word.find(ch)
        if i ==-1: return word
        return word[:i+1][::-1]+word[i+1:]