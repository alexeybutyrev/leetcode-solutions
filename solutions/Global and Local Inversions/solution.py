# Problem: Global and Local Inversions
# Language: python3
# Runtime: 332 ms
# Memory: 15.2 MB

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all(abs(i-x) <= 1 for i,x in enumerate(A))