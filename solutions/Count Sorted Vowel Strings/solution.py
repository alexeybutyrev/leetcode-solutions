# Problem: Count Sorted Vowel Strings
# Language: python3
# Runtime: 28 ms
# Memory: 14.2 MB

from math import comb
class Solution:
    def countVowelStrings(self, n: int) -> int:
        nw = 5
        return comb(n+4,n)
        def loop(ind, j):
            if j == n:
                return 1
            
            count = 0
            for i in range(ind, nw):
                count += loop(i, j+1)
            return count
        
        return loop(0, 0)
            
        