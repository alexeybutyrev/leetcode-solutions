# Problem: Rearrange K Substrings to Form Target String
# Language: python3
# Runtime: 263 ms
# Memory: 24.2 MB

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, K: int) -> bool:
        def makeCounter(S):
            N = len(S)
            c = Counter()
            k = N // K
            for i in range(N//k):
                c[S[i * k :(i + 1)*k]] += 1
            return c
        cS = makeCounter(s)
        cT = makeCounter(t)
        return cS == cT