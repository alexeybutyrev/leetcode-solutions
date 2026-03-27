# Problem: Largest 3-Same-Digit Number in String
# Language: python3
# Runtime: 44 ms
# Memory: 13.9 MB

from itertools import groupby
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        for s,l in groupby(num):
            #print(s,list(l))
            if len(list(l)) >= 3:
                ans = max(int(s), ans)
        return str(ans) * 3 if ans >= 0 else ""