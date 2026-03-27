# Problem: Valid Word
# Language: python3
# Runtime: 39 ms
# Memory: 16.6 MB

from string import ascii_lowercase, ascii_uppercase
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        V = set(['a', 'e', 'i', 'o', 'u'])
        C = set(ascii_lowercase) - V
        A = V | C | {'0','1','2','3','4','5','6','7','8','9'}
        
        for x in word:
            if x.lower() in V:
                break
        else:
            return False
        
        for x in word:
            if x.lower() in C:
                break
        else:
            return False

        for x in word:
            if x.lower() not in A:
                print(x)
                return False
        
        return True        
        
        