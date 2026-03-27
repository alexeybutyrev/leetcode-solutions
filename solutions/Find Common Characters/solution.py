# Problem: Find Common Characters
# Language: python3
# Runtime: 52 ms
# Memory: 16.6 MB

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])
        for w in words[1:]:
            c2 = Counter(w)
            for k in c:
                if k not in c2:
                    c[k] = 0
                c[k] = min(c[k], c2[k])
        ans = []
        
        for k,v in c.items():
            ans.extend( [k] * v)
        return ans