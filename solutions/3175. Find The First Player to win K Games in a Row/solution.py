# Problem: Find The First Player to win K Games in a Row
# Language: python3
# Runtime: 800 ms
# Memory: 31 MB

class Solution:
    def findWinningPlayer(self, A: List[int], k: int) -> int:
        N = len(A)
        if k >= N:
            # A.sort()
            
            return A.index(max(A))
        win = 0
        c = 0
        for i in range(1, N):
            if A[i] > A[win]:
                win = i
                c = 1
            else:
                c += 1
            if c == k:
                return win
        return A.index(max(A))
                
        
        