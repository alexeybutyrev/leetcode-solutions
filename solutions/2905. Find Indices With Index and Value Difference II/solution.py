# Problem: Find Indices With Index and Value Difference II
# Language: python3
# Runtime: 1645 ms
# Memory: 35.3 MB

from sortedcontainers import SortedList
class Solution:
    def findIndices(self, A: List[int], k: int, vD: int) -> List[int]:
        N = len(A)
        S = SortedList()
        
        for i,a in enumerate(A):
            if i >= k:
                S.add((a,i))
        if not S:
            return [-1,-1]
        for i,a in enumerate(A):
            if abs(a - S[-1][0]) >= vD:
                return [i,S[-1][1]]
            
            if abs(a - S[0][0]) >= vD:
                return [i,S[0][1]]
            S.remove((A[i+k], i+k))
            if not S: break
            
        
        
        return [-1,-1]