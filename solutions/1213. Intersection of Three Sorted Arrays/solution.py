# Problem: Intersection of Three Sorted Arrays
# Language: python3
# Runtime: 236 ms
# Memory: 12.8 MB

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        res = []
        for n in arr1:
            if n in arr2 and n in arr3:
                res.append(n)
        return res