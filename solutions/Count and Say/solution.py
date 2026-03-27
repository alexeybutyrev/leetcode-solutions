# Problem: Count and Say
# Language: python3
# Runtime: 48 ms
# Memory: 14.4 MB

from itertools import groupby
class Solution:
    def countAndSay(self, n: int) -> str:
        def f(s, n):
            if n == 0:
                return s
            s0 = ""
            for k,l in groupby(s):
                s0 += str(len(list(l))) + k
            return f(s0,n-1)
        
        return f("1",n-1)