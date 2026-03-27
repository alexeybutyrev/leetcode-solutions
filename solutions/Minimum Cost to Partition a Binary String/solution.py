# Problem: Minimum Cost to Partition a Binary String
# Language: python3
# Runtime: 1289 ms
# Memory: 240.5 MB


class Solution:
    def minCost(self, S: str, EC: int, FC: int) -> int:
        
        F = [0]

        for x in S:
            F.append(F[-1] + int(x))

        # Sij = F[j+1] - F[i]
        def walk(i,L):
            if L == 1:
                return EC if S[i] == '1' else FC
            X = F[i+L] - F[i]
            if X == 0:
                ans = FC
            else:
                ans = X * L * EC

            if L % 2 == 0:
                ans = min(ans, walk(i,L//2) + walk(i+L//2, L//2))
            
            return ans
        
        return walk(0, len(S))