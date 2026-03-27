# Problem: Sort the Matrix Diagonally
# Language: python3
# Runtime: 88 ms
# Memory: 14.7 MB

from collections import defaultdict
class Solution:
    def diagonalSort(self, M: List[List[int]]) -> List[List[int]]:
        n, m = len(M), len(M[0])
        nums = []
        
        hm = defaultdict(list)
        for i in range(n):
            for j in range(m):
                hm[i-j].append(M[i][j])
        
        for e in hm:
            hm[e].sort(reverse=True)
                
        for i in range(n):
            for j in range(m):
                M[i][j] = hm[i-j].pop()
        
        return M
       