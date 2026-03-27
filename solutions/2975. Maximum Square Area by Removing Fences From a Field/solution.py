# Problem: Maximum Square Area by Removing Fences From a Field
# Language: python3
# Runtime: 1437 ms
# Memory: 53.8 MB

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        H = [1] + hFences + [m]
        V = [1] + vFences + [n]
        H.sort()
        V.sort()

        def getLength(A):
            N = len(A)
            s = set()
            for i in range(N):
                for j in range(i+1,N):
                    s.add(A[j] - A[i])
            return s
        
        S = getLength(H) & getLength(V)
        if not S: return -1
        MOD = 10**9 + 7
        ans = -1
        for x in S:
            ans = max(ans, x * x)
        return ans % MOD