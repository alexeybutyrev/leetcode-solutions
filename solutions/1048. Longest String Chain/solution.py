# Problem: Longest String Chain
# Language: python3
# Runtime: 184 ms
# Memory: 14.4 MB

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        
        for w in sorted(words, key = len):
            dp[w] = 1
            for i in range(len(w)):
                nw = w[:i] + w[i+1:]
                c = 0 if nw not in dp else dp[nw]
                dp[w] = max(dp[w], c + 1)
        
        return max(dp.values())