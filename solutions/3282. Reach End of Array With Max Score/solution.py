# Problem: Reach End of Array With Max Score
# Language: python3
# Runtime: 1117 ms
# Memory: 31.8 MB

class Solution:
    def findMaximumScore(self, A: List[int]) -> int:
        n = {}
        N = len(A)
        
        curr = 0
        I = [0]
        n[0] = N-1
        for i in range(N):
            if A[i] > A[curr]:
                n[curr] = i
                curr = i
                n[curr] = N-1
                I.append(curr)
        
        ans = 0
        for x in I:
            ans += A[x] * (n[x] - x)
        
        return ans
