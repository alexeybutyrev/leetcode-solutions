# Problem: Min Max Game
# Language: python3
# Runtime: 87 ms
# Memory: 14.1 MB

class Solution:
    def minMaxGame(self, A: List[int]) -> int:
        i = 0
        while len(A) > 2:
            B = []
            #print(A)
            pr = True
            for i in range(1,len(A),2):
                if pr:
                    B.append(min(A[i],A[i-1]))
                else:
                    B.append(max(A[i],A[i-1]))
                pr = not pr
            A = B[:]
        
        return min(A)
                