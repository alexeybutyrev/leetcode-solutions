# Problem: Largest Combination With Bitwise AND Greater Than Zero
# Language: python3
# Runtime: 1323 ms
# Memory: 27.8 MB

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        N = 26
        cc = Counter()
        ans = 0
        for c in candidates:
            s = bin(c)[2:]
            s = '0' * (N - len(s)) + s
            for i in range(len(s)):
                if s[i] == '1':
                    cc[i] += 1
                    ans = max(ans, cc[i])
        return ans
            