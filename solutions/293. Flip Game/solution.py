# Problem: Flip Game
# Language: python3
# Runtime: 32 ms
# Memory: 14.5 MB

class Solution:
    def generatePossibleNextMoves(self, A: str) -> List[str]:
        
        ans = set()
        N = len(A)
        A = list(A)
        for i in range(N-1):
            if A[i] == A[i+1] == "+":
                A[i]   = "-"
                A[i+1] = "-"
                ans.add("".join(A))
                A[i]   = "+"
                A[i+1] = "+"
            
         
        
        return ans