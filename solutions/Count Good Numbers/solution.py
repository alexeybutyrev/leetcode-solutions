# Problem: Count Good Numbers
# Language: python3
# Runtime: 36 ms
# Memory: 14.3 MB

from math import log2
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def power(x, y, p) :
            res = 1     # Initialize result

            # Update x if it is more
            # than or equal to p
            x = x % p

            if (x == 0) :
                return 0

            while (y > 0) :

                # If y is odd, multiply
                # x with result
                if ((y & 1) == 1) :
                    res = (res * x) % p

                # y must be even now
                y = y >> 1      # y = y/2
                x = (x * x) % p
         
            return res

        odd, m = divmod(n,2)
        even = odd
        if m:
            odd +=1
        
        
        return (power(5, odd, MOD) %MOD * power(4, even, MOD) % MOD) % MOD
        
        