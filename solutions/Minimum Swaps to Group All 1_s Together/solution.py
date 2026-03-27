# Problem: Minimum Swaps to Group All 1's Together
# Language: python3
# Runtime: 744 ms
# Memory: 17.6 MB

from itertools import groupby
class Solution:
    def minSwaps(self, A: List[int]) -> int:
        
        Nz = sum(A)
        N = len(A)
        if Nz == N:
            return 0
        
        c = sum(A[0:Nz])
        
        ans = Nz - c
        for i in range(Nz, N):
            c -= A[i - Nz]
            c += A[i]
            
            ans = min(ans, Nz - c)
        
        
        return ans