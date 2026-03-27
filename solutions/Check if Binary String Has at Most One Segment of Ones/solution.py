# Problem: Check if Binary String Has at Most One Segment of Ones
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        c = Counter()
        for x,y in groupby(s):
            c[x] += 1
        return c['1'] == 1
        