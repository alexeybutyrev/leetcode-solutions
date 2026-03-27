# Problem: Element Appearing More Than 25% In Sorted Array
# Language: python3
# Runtime: 86 ms
# Memory: 18 MB

class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        N = len(A)
        c = Counter(A)
        
        for x,v in c.items():
            if v > N / 4:
                return x
            