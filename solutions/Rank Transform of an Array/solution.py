# Problem: Rank Transform of an Array
# Language: python3
# Runtime: 238 ms
# Memory: 37.9 MB

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hm = {}
        for i,x in enumerate(sorted(set(arr))):
            hm[x] = i
            
        return [hm[x] + 1 for x in arr]