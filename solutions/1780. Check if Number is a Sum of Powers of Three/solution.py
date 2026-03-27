# Problem: Check if Number is a Sum of Powers of Three
# Language: python3
# Runtime: 44 ms
# Memory: 14.3 MB

from math import log, floor
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        used = set()
        while n > 0:
            k = floor(log(n,3))
            
            if k in used:
                return False
            used.add(k)
            n -= 3**k
        return True