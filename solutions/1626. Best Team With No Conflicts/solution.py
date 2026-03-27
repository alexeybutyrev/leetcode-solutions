# Problem: Best Team With No Conflicts
# Language: python3
# Runtime: 5176 ms
# Memory: 69.4 MB

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        A = [(s,a) for s,a in zip(scores, ages)]
        A.sort()
        N = len(A)
        DP = [[-1] * (N+1) for _ in range(1001)]
        
        def dp(i,a):
            if DP[a][i] == -1:
                if i == N:
                    return 0
                s1 = 0
                if A[i][1] >= a:
                    s1 = A[i][0] + dp(i+1,A[i][1])
                s2 = dp(i+1,a)

                DP[a][i] = max(s1,s2)
            return DP[a][i]
        
        return dp(0,0)