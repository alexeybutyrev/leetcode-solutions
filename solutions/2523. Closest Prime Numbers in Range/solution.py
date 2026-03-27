# Problem: Closest Prime Numbers in Range
# Language: python3
# Runtime: 2386 ms
# Memory: 29 MB

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def SieveOfEratosthenes(num):
            prime = [True for i in range(num+1)]
            # boolean array
            p = 2
            while (p * p <= num):

                # If prime[p] is not
                # changed, then it is a prime
                if (prime[p] == True):

                    # Updating all multiples of p
                    for i in range(p * p, num+1, p):
                        prime[i] = False
                p += 1

            return prime
        
        prime = SieveOfEratosthenes(right)
        A = []
        for i in range(2,right+1):
             if i >= left and prime[i]:
                A.append(i)
        
        d = inf
        ans = [-1,-1]

        for i in range(len(A) - 1):
            if A[i+1] - A[i] < d:
                ans = [A[i],A[i+1]]
                d = A[i+1] - A[i]
        return ans
        