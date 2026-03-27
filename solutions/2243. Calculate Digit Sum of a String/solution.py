# Problem: Calculate Digit Sum of a String
# Language: python3
# Runtime: 43 ms
# Memory: 14 MB

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s0 = ''
            for i in range(0,len(s),k):
                l = s[i:i+k]
                a = 0
                for d in l:
                    a += int(d)
                s0 = s0 + str(a)
            s = s0
        return s