# Problem: Minimum Number of Moves to Seat Everyone
# Language: python3
# Runtime: 87 ms
# Memory: 14.2 MB

class Solution:
    def minMovesToSeat(self, S: List[int], A: List[int]) -> int:
        S.sort()
        A.sort()
        ans = 0
        for s,a in zip(S,A):
            ans += abs(s - a)
        return ans
        