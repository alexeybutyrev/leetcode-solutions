# Problem: Minimum Number of Operations to Make Arrays Similar
# Language: python3
# Runtime: 994 ms
# Memory: 32.6 MB

class Solution:
    def makeSimilar(self, A: List[int], B: List[int]) -> int:
        O1 = sorted([a for a in A if a & 1])
        O2 = sorted([a for a in B if a & 1])
        
        E1 = sorted([a for a in A if (a & 1) == 0])
        E2 = sorted([a for a in B if (a & 1) == 0])
        
        c1 = sum( abs(x - y) // 2 for x,y in zip(O1,O2))
        c2 = sum( abs(x - y) // 2 for x,y in zip(E1,E2))
        return (c1 + c2) // 2