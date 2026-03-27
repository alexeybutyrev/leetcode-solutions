# Problem: Can Place Flowers
# Language: python3
# Runtime: 170 ms
# Memory: 14.4 MB

class Solution:
    def canPlaceFlowers(self, A: List[int], n: int) -> bool:
        if n == 0: return True
        N = len(A)
        if N == 1: return A[0] == 0 and n == 1
        
        for i in range(N-1):

            if i == 0 and A[i] == A[i+1] == 0:
                A[i] = 1
                n -= 1
            if i > 0:
                if A[i-1] == A[i+1] == A[i] == 0:
                    A[i] = 1
                    n-=1
            
            if n == 0:

                return True
        if A[N-1] == A[N-2] == 0:
            n-=1
            
        return 0 == n
                        
            