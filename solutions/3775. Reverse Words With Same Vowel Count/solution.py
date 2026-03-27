# Problem: Reverse Words With Same Vowel Count
# Language: python3
# Runtime: 127 ms
# Memory: 24 MB

class Solution:
    def reverseWords(self, s: str) -> str:
        V = {'a', 'e', 'i', 'o', 'u'}

        W = s.split(" ")
        count = {}
        ans = [W[0]]
        c = 0
        for x in W[0]:
            if x in V:
                c += 1
        
        for w in W[1:]:
            c1 = 0
            for x in w:
                if x in V:
                    c1 += 1
            if c1 == c:
                ans.append(w[::-1])
            else:
                ans.append(w)
        
        return " ".join(ans)