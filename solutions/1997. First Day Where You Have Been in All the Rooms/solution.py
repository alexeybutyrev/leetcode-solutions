# Problem: First Day Where You Have Been in All the Rooms
# Language: python3
# Runtime: 1662 ms
# Memory: 29.1 MB

class Solution:
    def firstDayBeenInAllRooms(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(A)
        dp = [0] * N
        for i in range(1,N):
            dp[i] = (2 * dp[i-1] - dp[A[i-1]] + 2) % MOD
        return dp[-1]