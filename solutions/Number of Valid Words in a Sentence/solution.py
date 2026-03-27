# Problem: Number of Valid Words in a Sentence
# Language: python3
# Runtime: 104 ms
# Memory: 14.5 MB

class Solution:
    def countValidWords(self, sentence: str) -> int:
        count = 0
        for w in sentence.split(" "):
            if w:
                c = Counter(w)
                pr = True
                for i in range(10):
                    if str(i) in c:
                        pr = False
                        break
                if not pr:
                    continue
                
                if c['.'] > 1 or c['!'] > 1 or c[','] > 1 or c['-'] > 1:
                    continue
                
                
                for ch in ['.',',','!']:
                    if ch in w and w[-1] != ch:
                        pr = False
                        break
                
                if not pr:
                    continue
                
                for ch in ['.',',','!']:
                    if ch in w and w[-1] == ch:
                        w = w[:-1]
                if not w:
                    count += 1
                    continue
                    
                if '-' in w and w[-1] =='-' or w[0] == '-':
                    continue

                count +=1
        return count
                
                