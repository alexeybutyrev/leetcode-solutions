# Problem: Range Addition II
# Language: python3
# Runtime: 60 ms
# Memory: 16.1 MB

class Solution:
    def maxCount(self, m: int, n: int, A: List[List[int]]) -> int:
        if not A:
            return m * n 
        
        return min(map(lambda x: x[0], A)) * min(map(lambda x: x[1], A))