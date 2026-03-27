# Problem: Stone Game VI
# Language: python3
# Runtime: 1340 ms
# Memory: 29.6 MB

class Solution:
    def stoneGameVI(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        
        C = [ (a+b,i) for i, (a,b) in enumerate(zip(A, B))]
        C.sort()
        vals = [0] * 2
        k = 0
        while C:
            _, ind = C.pop()
            vals[k % 2] += A[ind] if k % 2 == 0 else B[ind]
            k += 1
            
        if vals[0] == vals[1]:
            return 0 
        
        return 1 if vals[0] > vals[1] else -1
            
        
        
        