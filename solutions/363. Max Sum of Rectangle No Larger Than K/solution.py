# Problem: Max Sum of Rectangle No Larger Than K
# Language: python3
# Runtime: 9960 ms
# Memory: 15.4 MB

from sortedcontainers import SortedSet
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], K: int) -> int:
        R = []
        for r in matrix:
            R.append(list(accumulate(r,initial = 0)))
        #print(R)
        A = []
        for c in zip(*R):
            A.append(list(accumulate(c,initial = 0)))
        
       
        def area(i,j,k,l):
            return A[i][j] + A[k][l] - A[i][l] - A[k][j]
        
        M = len(A[0])
        
        def search(B,x):
            S = SortedSet()
            ans = -inf
            for i in range(len(B)):
                ind = S.bisect_left(B[i] - x)
                if ind < len(S):
                    ans = max(ans, B[i] - S[ind])
                S.add(B[i])    
            return ans
                        
                    
            
        ans = -inf
        for i1 in range(N:=len(A)):
            for i2 in range(i1+1,N):
                B = [b - a for a,b in zip(A[i1],A[i2])]
                ans = max(ans, search(B,K))
                
        
        return ans
        
                