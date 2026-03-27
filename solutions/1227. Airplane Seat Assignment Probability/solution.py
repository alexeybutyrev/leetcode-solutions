# Problem: Airplane Seat Assignment Probability
# Language: python3
# Runtime: 39 ms
# Memory: 16.4 MB

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1: return 1
        return 0.5