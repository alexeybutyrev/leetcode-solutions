# Problem: Reordered Power of 2
# Language: python
# Runtime: 16 ms
# Memory: 13.5 MB

from math import log
class Solution(object):
    def __init__(self):
        self.s = set()
        self.s.add("1")
        c = 0
        K = 1
        while K <= 10** 9:
            K *= 2
            self.s.add("".join(sorted(str(K))))
            
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return "".join(sorted(str(N))) in self.s