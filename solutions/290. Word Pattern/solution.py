# Problem: Word Pattern
# Language: python3
# Runtime: 28 ms
# Memory: 13.9 MB

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        S = s.split(" ")
        if len(S) != len(pattern):
            return False
        d = {}
        seen = set()
        for l,word in zip(pattern, S):
            if l not in d and word not in seen:
                d[l] = word
                seen.add(word)
            else:
                if l in d and d[l] == word:
                    continue
                return False
        return True