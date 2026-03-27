# Problem: Transpose Matrix
# Language: python3
# Runtime: 68 ms
# Memory: 14.8 MB

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return list(zip(*A))