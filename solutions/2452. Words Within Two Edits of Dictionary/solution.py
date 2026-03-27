# Problem: Words Within Two Edits of Dictionary
# Language: python3
# Runtime: 260 ms
# Memory: 14.1 MB

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def hamming(a,b):
            return sum(x!=y for x,y in zip(a,b))
        ans = []
        for w in queries:
            for d in dictionary:
                if hamming(w,d) <= 2:
                    ans.append(w)
                    break
        return ans