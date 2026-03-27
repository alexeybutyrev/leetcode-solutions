# Problem: Delete Characters to Make Fancy String
# Language: python3
# Runtime: 540 ms
# Memory: 16.9 MB

from itertools import groupby
class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ''
        
        for k,l in groupby(s):
            ln = len(list(l))
            if ln < 3:
                ans += k * ln
            else:
                ans += k * 2
        return ans