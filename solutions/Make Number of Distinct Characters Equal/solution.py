# Problem: Make Number of Distinct Characters Equal
# Language: python3
# Runtime: 573 ms
# Memory: 15.2 MB

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = [0] * 26
        c2 = [0] * 26
        
        d1 = set()
        for l in word1:
            c1[ord(l) - ord('a')] += 1
            d1.add(ord(l) - ord('a'))
        
        d2 = set()
        for l in word2:
            c2[ord(l) - ord('a')] += 1
            d2.add(ord(l) - ord('a'))
        
        for i in range(26):
            if c1[i]:
                if c1[i] == 1: d1.remove(i)
                for j in range(26):
                    if c2[j]:
                        if c2[j] == 1:
                            if len( d2 - {j} | {i}) == len(d1 | {j}):
                                return True
                        else:
                            if len(d2 | {i}) == len(d1 | {j}):
                                return True
                        
                d1.add(i)
        
        return False