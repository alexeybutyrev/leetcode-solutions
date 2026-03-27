# Problem: Arithmetic Slices
# Language: python3
# Runtime: 44 ms
# Memory: 14.8 MB


    
class Solution:
    def __init__(self):
        self.F = [0]
        for i in range(1,5001):
            self.F.append(self.F[-1] + i)
            
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        
        def f(x):
            if x < 3: return 0
            return self.F[x-2]
        
        N = len(A)
        if N < 3:
            return 0
        
        d = A[1] - A[0]
        c = 2
        ans = 0
        for i in range(2,N):
            if A[i] - A[i-1] == d:
                c += 1
            else:
                ans += f(c)
                c = 2
                d = A[i] - A[i-1]
                
        return ans + f(c)