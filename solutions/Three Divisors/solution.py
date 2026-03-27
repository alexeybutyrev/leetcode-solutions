# Problem: Three Divisors
# Language: python3
# Runtime: 32 ms
# Memory: 14.3 MB

class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(1,n+1):
            if n % i == 0:
                count += 1
                if count > 3:
                    return False
        return count == 3
            