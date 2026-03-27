# Problem: Find the Winner of the Circular Game
# Language: python3
# Runtime: 92 ms
# Memory: 14.4 MB

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        A = list(range(1,n+1))
        ind = 0
        while len(A) > 1:
            N = len(A)
            
            ind += k % N - 1
            ind %= N
            x = A[ind]
            A.remove(x)
    
        return A[0]