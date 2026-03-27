# Problem: Lonely Pixel I
# Language: python3
# Runtime: 1206 ms
# Memory: 14.9 MB

class Solution:
    def findLonelyPixel(self, A: List[List[str]]) -> int:
        # sum "B" in rows
        R = [sum(1 for c in r if c == "B") for r in A]
        
        # sum "B" in cols
        C = [sum(1 for r in c if r == "B") for c in zip(*A)]
        
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans += (A[i][j] == "B" and R[i] == C[j] == 1)
                    
        return ans
        