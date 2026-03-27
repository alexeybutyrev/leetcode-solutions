# Problem: Predict the Winner
# Language: python3
# Runtime: 55 ms
# Memory: 14.1 MB

class Solution:
    def PredictTheWinner(self, A: List[int]) -> bool:
        S = sum(A)
        N = len(A)
        @cache
        def dp(i,j):
            if i == j:
                return A[i]
            return max(A[i] - dp(i+1,j), A[j] - dp(i,j-1))
        
        return dp(0,len(A) - 1) >= 0