# Problem: Sentence Similarity
# Language: python3
# Runtime: 51 ms
# Memory: 14 MB

class Solution:
    def areSentencesSimilar(self, S1: List[str], S2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(S1) != len(S2):
            return False
        
        s = set()
        for u,v in similarPairs:
            s.add((u,v))
            s.add((v,u))
        
        return all( (l1,l2) in s or l1 == l2 for l1,l2 in zip(S1,S2))
