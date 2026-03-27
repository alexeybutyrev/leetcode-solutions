# Problem: Keyboard Row
# Language: python3
# Runtime: 61 ms
# Memory: 13.8 MB

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        c1 = set("qwertyuiop")
        c2 = set("asdfghjkl")
        c3 = set("zxcvbnm")
        ans = []
        for w in words:
            s = set(w.lower())
            if not s -c1 or not s-c2 or not s - c3:
                ans.append(w)
        return ans