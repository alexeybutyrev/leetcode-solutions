# Problem: Eliminate Maximum Number of Monsters
# Language: python3
# Runtime: 1048 ms
# Memory: 30.2 MB

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        A = sorted([d/v for d,v in zip(dist, speed)])
        
        for i,a in enumerate(A):
            if a <= i:
                return i
        return len(A)
            
            