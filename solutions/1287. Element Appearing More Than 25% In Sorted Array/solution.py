# Problem: Element Appearing More Than 25% In Sorted Array
# Language: python3
# Runtime: 92 ms
# Memory: 15.7 MB

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        
        for k,v in c.items():
            if v > len(arr) / 4:
                return k
        