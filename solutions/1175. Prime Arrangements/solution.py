# Problem: Prime Arrangements
# Language: python3
# Runtime: 32 ms
# Memory: 14.2 MB

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 2:
            return 1
        def num_primes(n):
            if n <= 2:
                return 0

            s = set()
            for p in range(2, 1 + int(sqrt(n))):
                if p not in s:
                    for j in range(p*p, n, p):
                        s.add(j)
            return n - len(s) - 2
        K = num_primes(n+1)
        
        
        MOD = 1_000_000_007
        F1 = factorial(K) % MOD
        F2 = factorial(n - K)% MOD
        return (F1 * F2) % MOD