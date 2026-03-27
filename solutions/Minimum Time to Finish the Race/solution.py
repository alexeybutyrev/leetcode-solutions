# Problem: Minimum Time to Finish the Race
# Language: python3
# Runtime: 6039 ms
# Memory: 50.8 MB

class Solution:
    def minimumFinishTime(self, A: List[List[int]], C: int, L: int) -> int:
        G = [inf] * 19
        
        for f,r in A:
            tot = curr = f
            G[1] = min(G[1],tot)
            for i in range(2,19):
                curr *= r
                tot += curr
                if tot > 2e5:
                    break
                G[i] = min(G[i],tot)
        
        DP = [0] * (L+1)
        
        for i in range(1,L+1):
            DP[i] = G[i] if i < 19 else inf
            for j in range(1,i//2 + 1):
                DP[i] = min(DP[i], DP[j] + C + DP[i-j])
        return DP[-1]