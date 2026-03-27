# Problem: Check if One String Swap Can Make Strings Equal
# Language: python3
# Runtime: 0 ms
# Memory: 17.6 MB

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2) and sum(x!=y for x,y in zip(s1,s2)) in {2,0}