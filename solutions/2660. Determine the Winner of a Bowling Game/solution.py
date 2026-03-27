# Problem: Determine the Winner of a Bowling Game
# Language: python3
# Runtime: 279 ms
# Memory: 16.4 MB

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        def count(A):
            N = len(A)
            s = A[0]
            for i in range(1,N):
                if i == 1:
                    if A[i-1] == 10:
                        s += A[i] * 2
                    else:
                        s += A[i]
                else:
                    if A[i-2] == 10 or A[i-1] == 10:
                        s += A[i] * 2
                    else:
                        s += A[i]
            return s
        
        s1 = count(player1)
        s2 = count(player2)
        
        if s1 == s2: return 0
        
        return 1 if s1 > s2 else 2