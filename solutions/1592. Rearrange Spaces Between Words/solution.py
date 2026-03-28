# Problem: Rearrange Spaces Between Words
# Language: python3
# Runtime: 24 ms
# Memory: 14.3 MB

class Solution:
    def reorderSpaces(self, text: str) -> str:
        N = len(text)
        words = []
        w = ''
        ns = 0
        for i,l in enumerate(text):
            if l != ' ':
                w += l
            else:
                ns += 1
                if w:
                    words.append(w)
                    w = ''
        if not ns:
            return text
        
        if w:
            words.append(w)
        
        if len(words) == 1:
            return words[0] + ' ' * ns
        k = ns // (len(words) -1)
        
        ans = words[0]
        for i in range(1,len(words)):
            ans += k * ' ' + words[i]
        
        return ans + ' ' * (ns - k * (len(words) - 1))