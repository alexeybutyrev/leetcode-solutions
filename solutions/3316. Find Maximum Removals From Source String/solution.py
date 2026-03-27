# Problem: Find Maximum Removals From Source String
# Language: python3
# Runtime: 4303 ms
# Memory: 89 MB

class Solution:
    def maxRemovals(self, S: str, P: str, T: List[int]) -> int:
        
        NP = len(P)
        NS = len(S)
        
        DP = [[-1] * NP for _ in range(NS)]

        def dp(i,j):
            if j == NP: 
                ind = bisect_left(T,i)
                return len(T) - ind
            if i == NS: return -inf
            
            
            if DP[i][j] == -1:
            
                ans = dp(i+1,j)
                if S[i] == P[j]:
                    ans = max(ans, dp(i+1,j+1))

                ind = bisect_left(T,i)
                if ind != len(T) and T[ind] == i:
                    # remove
                    ans = max(ans,1 + dp(i+1,j))
                DP[i][j] = ans
            return DP[i][j]
        return dp(0,0)

            