# Problem: Maximum Xor Product
# Language: python3
# Runtime: 39 ms
# Memory: 16.3 MB

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10**9 + 7
        x = 0
        for  i in range(n-1,-1,-1):
            if (a & (1 << i)) == (b & (1 <<i)):
                a |= (1<<i)
                b |= (1<<i)
                
            else:
                mask = ~(1 <<i)
                if a < b:
                    a |= (1<<i)
                    b &= mask
                else:
                    b |= (1<<i)
                    a &= mask
                    
        return (a * b) % MOD
                