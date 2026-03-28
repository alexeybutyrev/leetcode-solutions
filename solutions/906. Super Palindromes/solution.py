# Problem: Super Palindromes
# Language: python3
# Runtime: 772 ms
# Memory: 14.3 MB

from math import sqrt
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        is_pali = lambda x: x == x[::-1]
        
        
        count = 0
        L, R = int(left), int(right)
        for i in range(100000):
            s = str(i)
            t = s + s[-2::-1]
            n = int(t) ** 2
            if n > R: 
                break
            if n >= L and is_pali(str(n)):
                count +=1

        for i in range(100000):
            s = str(i)
            t = s + s[::-1]
            n = int(t) ** 2
            if n > R: 
                break
            if n >= L and is_pali(str(n)):
                count +=1

        
        return count
            