# Problem: Check Distances Between Same Letters
# Language: python3
# Runtime: 66 ms
# Memory: 13.8 MB

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i,d in enumerate(distance):
        
            i1 = s.find(chr(i + ord('a')),0)
            if i1 == -1:
                continue
            
            i2 = s.find(chr(i + ord('a')),i1+1)
            if i2 - i1-1 != d:
                return False
            
        return True