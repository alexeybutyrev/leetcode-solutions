# Problem: Factor Combinations
# Language: python3
# Runtime: 104 ms
# Memory: 15.1 MB

from itertools import product
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        q = [(n,2,[])]
        ans = []
        
        while q:
            n, i, c = q.pop()
            
            while i * i <= n:
                if n % i == 0:
                    ans.append(  c + [i, n // i])
                    q.append((n//i,i,c + [i]))
                i+=1

        return ans