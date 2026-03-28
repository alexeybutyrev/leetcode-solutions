# Problem: Rearrange Words in a Sentence
# Language: python3
# Runtime: 84 ms
# Memory: 17.4 MB

class Solution:
    def arrangeWords(self, text: str) -> str:
        
        words = text.split(" ")
        lenght = []
        for w in words:
            lenght.append(len(w))
        
        
        keys = [words[i[0]].lower() for i in sorted(enumerate(lenght), key=lambda x:x[1])]
        
        s = keys[0].title()
        n = len(keys)
        if 1 == n:
            return s
        
        for i in range(1,n):
            s+= " " + keys[i]
        return s
            
                