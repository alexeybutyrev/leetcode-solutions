# Problem: Minimum Sideway Jumps
# Language: python3
# Runtime: 4428 ms
# Memory: 717.5 MB

class Solution:
    def minSideJumps(self, A: List[int]) -> int:
        sys.setrecursionlimit(10**7)
        N = len(A)
        dp = [[-1] * 3 for _ in range(N)]
        
        def walk(i, ln):
            if i == N -1:
                return 0
                        
            if dp[i][ln-1] < 0:
                if A[i+1] == ln:
                    v = inf
                    for j in range(1,4):
                        if j != ln and A[i] != j:
                            v = min(v, 1 + walk(i+1, j))
                    dp[i][ln-1] = v
                else:
                    dp[i][ln-1] = walk(i+1, ln)
            
            return  dp[i][ln-1]
            
        return walk(0, 2)