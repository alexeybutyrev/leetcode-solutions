# Problem: Nth Digit
# Language: python3
# Runtime: 33 ms
# Memory: 16.3 MB

class Solution:
    def findNthDigit(self, n: int) -> int:
        n-=1
        
        for d in range(1,11):
            f = 10**(d-1)
            if n < 9 * f * d:
                return int(str(f + n//d)[n%d])
            n -= 9 * f * d
        