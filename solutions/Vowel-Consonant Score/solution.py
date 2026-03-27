# Problem: Vowel-Consonant Score
# Language: python3
# Runtime: 0 ms
# Memory: 19.6 MB

class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        V = set(['a', 'e', 'i', 'o', 'u'])
        v = c = 0

        for x in s:
            if x.isalpha():
                if x in V:
                    v += 1
                else:
                    c += 1
        if c:
            return floor(v/c)
        return 0