# Problem: Powerful Integers
# Language: python3
# Runtime: 24 ms
# Memory: 14.3 MB

from math import log, ceil
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        hx = {0:1}
        hy = {0:1}
        MX = 1 if x == 1 else ceil(log(bound,x))
        MY = 1 if y == 1 else ceil(log(bound,y))
        ans = set()
        for i in range(MX):
            if i > 0 and i not in hx:
                hx[i] = hx[i-1] * x
            for j in range(MY):
                if j > 0 and j not in hy:
                    hy[j] = hy[j-1] * y
                if hx[i] + hy[j] <= bound:
                    ans.add(hx[i]+hy[j])
                else:
                    break

        return ans
                
            