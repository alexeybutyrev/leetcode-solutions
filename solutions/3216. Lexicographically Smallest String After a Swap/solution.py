# Problem: Lexicographically Smallest String After a Swap
# Language: python3
# Runtime: 34 ms
# Memory: 16.5 MB

class Solution:
    def getSmallestString(self, s: str) -> str:
        ans = s
        S = list(s)
        for i in range(1,len(s)):
            if (int(S[i]) % 2) == (int(S[i-1]) % 2):
                S[i],S[i-1] = S[i-1], S[i]
                ans = min(ans, "".join(S))
                S[i],S[i-1] = S[i-1], S[i]
        return ans