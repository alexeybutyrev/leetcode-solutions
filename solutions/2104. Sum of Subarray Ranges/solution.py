# Problem: Sum of Subarray Ranges
# Language: python3
# Runtime: 8107 ms
# Memory: 29.7 MB

class Solution:
    def subArrayRanges(self, A: List[int]) -> int:
        #A.sort()
        N = len(A)
        ans = 0
        
        MIN = [[0] * N for _ in range(N)]
        MAX = [[0] * N for _ in range(N)]
        
        for i in range(N):
            MIN[i][i] = A[i]
            MAX[i][i] = A[i]
            
        for i in range(N):    
            for j in range(i+1,N):
                MIN[i][j] = min(MIN[i][j-1], A[j])
                MAX[i][j] = max(MAX[i][j-1], A[j])
                ans += MAX[i][j] - MIN[i][j]
        return ans