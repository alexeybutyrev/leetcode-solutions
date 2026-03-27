# Problem: Sentence Similarity II
# Language: python3
# Runtime: 826 ms
# Memory: 15.5 MB

class Solution:
    def areSentencesSimilarTwo(self, S1: List[str], S2: List[str], similarPairs: List[List[str]]) -> bool:
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        for u,v in similarPairs:
            union(u,v)
        
        N1 = len(S1)
        N2 = len(S2)
        if N1 != N2:
            return False
        
        for i in range(N1):
            if S1[i] == S2[i]:
                continue
            if (S1[i] not in UF or S2[i] not in UF) or (find(S1[i]) != find(S2[i])):
                return False
        return True