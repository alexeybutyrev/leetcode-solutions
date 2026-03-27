# Problem: Maximum Points After Enemy Battles
# Language: python3
# Runtime: 432 ms
# Memory: 31.7 MB

class Solution:
    def maximumPoints(self, A: List[int], E: int) -> int:
        m = min(A)
        if E < m:
            return 0
        S = sum(A) - m + E
        return S // m

        