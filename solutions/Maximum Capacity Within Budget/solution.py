# Problem: Maximum Capacity Within Budget
# Language: python3
# Runtime: 486 ms
# Memory: 42.6 MB

from sortedcontainers import SortedDict
class Solution:
    def maxCapacity(self, P: List[int], C: List[int], B: int) -> int:
        A = [ (p,c) for p,c in zip(P,C)]
        A.sort()
        N = len(A)
        W = [0] * N

        curr = 0
        for i,(p,c) in enumerate(A):
            curr = max(c,curr)
            W[i] = curr

        P.sort()
        ans = 0

        for i,(p, c) in  enumerate(A):
            if p >= B: break

            ans = max(ans, c)

            ind = min(i, bisect_left(P, B - p))-1
            if ind >=0:
                ans = max(ans, W[ind] + c)
        


        return ans

        
            
        
                
            
            
            