# Problem: Prime Pairs With Target Sum
# Language: python3
# Runtime: 5963 ms
# Memory: 25.1 MB

def generate_primes(n):
    primes = set()
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(num)
    return primes

P = generate_primes(10**6)
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        mn = n + 1
        ans = []
        for num in range(2, n+1):
            if num >= mn: break
            is_prime = True
            if num in P:
                if n - num in P:
                    mn = min(mn, n - num)
                    ans.append([num, n - num])
            
            
        return ans