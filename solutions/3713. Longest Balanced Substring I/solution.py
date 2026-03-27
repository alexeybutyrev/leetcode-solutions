# Problem: Longest Balanced Substring I
# Language: python3
# Runtime: 3201 ms
# Memory: 19.3 MB

class Solution:
    def longestBalanced(self, S: str) -> int:
        N = len(S)
        ans = 0
        for i in range(N):
            C = Counter()
            for j in range(i,N):
                C[S[j]] += 1
                if len(set(C.values())) == 1:
                    ans = max(ans, j - i + 1)
        return ans
            