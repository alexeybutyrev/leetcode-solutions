# Problem: Minimum Cost to Equalize Arrays Using Swaps
# Language: python3
# Runtime: 271 ms
# Memory: 47.8 MB

class Solution:
    def minCost(self, A: list[int], B: list[int]) -> int:
        cA = Counter(A)
        cB = Counter(B)

        x = set(cA.keys()) | set(cB.keys())

        A = []
        B = []
        for a in x:
            if (cA[a] + cB[a]) & 1: return -1
            if cA[a] != cB[a]:
                A.append(cA[a])
                B.append(cB[a])

        ans = 0
        for x,y in zip(A,B):
            ans += abs(x-y) // 2
        return ans // 2