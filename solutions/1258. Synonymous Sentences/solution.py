# Problem: Synonymous Sentences
# Language: python3
# Runtime: 35 ms
# Memory: 13.9 MB

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        UF = {}
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        words = set()
        for u,v in synonyms:
            union(u,v)
            words.add(u)
            words.add(v)
        
        groups = defaultdict(set)
        
        for w in words:
            groups[find(w)].add(w)
        
        text = text.split(" ")
        N = len(text)
        self.ans = []
        def backtrack(i,t):
            if i == N:
                self.ans.append(" ".join(t))
            else:
                if text[i] in words:
                    for w in groups[find(text[i])]:
                        backtrack(i+1, t + [w])
                else:
                    backtrack(i+1, t + [text[i]])
        backtrack(0,[])
        return sorted(self.ans)
            
            