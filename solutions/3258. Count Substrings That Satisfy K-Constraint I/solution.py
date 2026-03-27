# Problem: Count Substrings That Satisfy K-Constraint I
# Language: python3
# Runtime: 62 ms
# Memory: 16.5 MB

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        for i in range(N:=len(s)):
            z = 0
            o = 0
            for j in range(i,N):
                if s[j] == '0':
                    z += 1
                else:
                    o += 1
                if z > k and o > k:
                    break
                ans += 1
        return ans
