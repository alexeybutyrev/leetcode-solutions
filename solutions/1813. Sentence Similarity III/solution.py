# Problem: Sentence Similarity III
# Language: python3
# Runtime: 32 ms
# Memory: 14.4 MB

class Solution:
    def areSentencesSimilar(self, S1: str, S2: str) -> bool:
        
        S1 = S1.split(" ")
        S2 = S2.split(" ")
        if len(S1) < len(S2):
            S1, S2 = S2, S1
        
        N1 = len(S1)
        N2 = len(S2)
        
        S2 = deque(S2)
        # begining
        
        i = 0
        while S2 and S1[i] == S2[0]:
            S2.popleft()
            i+=1
        
        i = N1-1
        while S2 and S1[i] == S2[-1]:
            S2.pop()
            i-=1
        
        return len(S2) == 0