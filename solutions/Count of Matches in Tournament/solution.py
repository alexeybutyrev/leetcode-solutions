# Problem: Count of Matches in Tournament
# Language: python3
# Runtime: 40 ms
# Memory: 14.2 MB

class Solution:
    def numberOfMatches(self, n: int) -> int:
        s = 0
        
        while n > 1:
            if n % 2 == 0:
                n = n // 2
                s += n
            else:
                s += (n - 1) // 2
                n = (n - 1) // 2 + 1
        
        return s