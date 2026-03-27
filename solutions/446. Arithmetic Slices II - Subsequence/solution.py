# Problem: Arithmetic Slices II - Subsequence
# Language: python3
# Runtime: 595 ms
# Memory: 55.9 MB


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = 0
        dp = defaultdict(Counter)
        for i in range(len(A)):
            for j in range(i):
                dp[i][A[i] - A[j]] += 1
                if A[i]-A[j] in dp[j]:
                    dp[i][A[i] - A[j]] += dp[j][A[i]-A[j]]
                    ans += dp[j][A[i]-A[j]]
        return ans