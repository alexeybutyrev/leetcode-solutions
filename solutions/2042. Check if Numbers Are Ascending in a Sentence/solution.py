# Problem: Check if Numbers Are Ascending in a Sentence
# Language: python3
# Runtime: 28 ms
# Memory: 14.1 MB

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        d = -1
        i = 0 
        N = len(s)
        while i < N:
            c = ''
            while i < N and s[i].isdigit():
                c+= s[i]
                i+=1
            if c:    
                if int(c) <= d:
                    return False
                d = int(c)
            i+=1
        return True