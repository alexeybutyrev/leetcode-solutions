# Problem: Minimum Moves to Equal Array Elements II
# Language: python3
# Runtime: 148 ms
# Memory: 15.3 MB

class Solution:
    def minMoves2(self, A: List[int]) -> int:
        x = round(median(A))
        f = lambda x: sum(abs(x-a)for a in A)
        return min(f(x),f(x-1),f(x+1))