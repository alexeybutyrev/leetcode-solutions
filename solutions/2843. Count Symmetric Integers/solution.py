# Problem:   Count Symmetric Integers
# Language: python3
# Runtime: 930 ms
# Memory: 16.3 MB

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for x in range(low, high+1):
            s = str(x)
            N = len(s)
            if N & 1: continue
            s1 = sum(int(x) for x in s[:N//2])
            s2 = sum(int(x) for x in s[N//2:])
            ans += int(s1 == s2)
        return ans