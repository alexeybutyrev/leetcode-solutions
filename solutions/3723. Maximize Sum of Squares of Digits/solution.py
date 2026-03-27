# Problem: Maximize Sum of Squares of Digits
# Language: python3
# Runtime: 353 ms
# Memory: 20.4 MB

class Solution:
    def maxSumOfSquares(self, N: int, S: int) -> str:

        if N * 9 < S: return ""
        ans = ""

        while S > 9:
            ans += "9"
            S -= 9
            N -= 1

        if S:
            ans += str(S)
            N -= 1
        if N:
            ans += '0' * N
        return ans