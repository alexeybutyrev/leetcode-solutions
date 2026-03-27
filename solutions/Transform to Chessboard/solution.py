# Problem: Transform to Chessboard
# Language: python3
# Runtime: 80 ms
# Memory: 14.5 MB

from itertools import permutations
class Solution:
    def movesToChessboard(self, A: List[List[int]]) -> int:
        N = len(A)
        if N <= 1:
            return 0
        
        rows = ["".join(str(c) for c in r) for r in A]
        c = Counter(rows)
        keys = list(c.keys())
        if (len(keys) != 2 or abs(c[keys[0]] - c[keys[1]]) > 1
            or abs(keys[0].count('1') - keys[0].count('0')) > 1 
            or any(a==b for a,b in zip(*keys))
           ):
            return -1
        
        rowdiff = sum(A[0][i] != (i%2) for i in range(N))
        coldiff = sum(A[i][0] != (i%2) for i in range(N))
        
        rowdiff=N-rowdiff if rowdiff%2 !=0 or (N%2==0 and (N-rowdiff)<rowdiff) else rowdiff
        coldiff=N-coldiff if coldiff%2 !=0 or (N%2==0 and (N-coldiff)<coldiff) else coldiff
        return (rowdiff+coldiff)//2
            
                        
        
        