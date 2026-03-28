# Problem: Count Primes
# Language: python3
# Runtime: 1920 ms
# Memory: 52.7 MB

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        def is_prime(num):
            if num <= 1:
                return False
            i = 2
            while i * i <= num:
                if num % i == 0:
                    return False
                i+=1
            return True
        

        iPrime = [True] * (n)  
        iPrime[0] = False    # 0
        iPrime[1] = False    # 1
        
        for i in range(2, int(sqrt(n)) + 1 ):
            if iPrime[i]:
                if is_prime(i):
                    for j in range(i,n):
                        c = j * i
                        if c >= n:
                            break
                        else:
                            iPrime[c] = False
                else:
                    iPrime[i] = False
        
        
        return sum(iPrime)
            