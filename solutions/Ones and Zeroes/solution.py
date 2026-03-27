# Problem: Ones and Zeroes
# Language: python3
# Runtime: 2000 ms
# Memory: 296.4 MB

from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        A = []
        for s in strs:
            c = Counter(s)
            A.append((c["0"], c["1"]))
        
        N = len(A)
        #print(A)
        @lru_cache(None)
        def count_len(i, nzeros, nones):
            
            if i == N or (nzeros < 0 or nones < 0):
                return 0
            
            c1 = count_len(i + 1, nzeros, nones)
            c2 = 0
            if nzeros >= A[i][0] and nones >= A[i][1]:
                c2 = 1 + count_len(i + 1, nzeros - A[i][0], nones - A[i][1])
            
            return max(c1, c2)
        
        return count_len(0, m, n)