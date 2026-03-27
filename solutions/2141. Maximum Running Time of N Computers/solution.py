# Problem: Maximum Running Time of N Computers
# Language: python3
# Runtime: 63 ms
# Memory: 31.2 MB

class Solution:
    def maxRunTime(self, n: int, A: List[int]) -> int:
        A.sort(reverse=True)
        s = sum(A)
        for a in A:
            if a > s // n:
                n -= 1
                s -= a
            else:
                return s // n