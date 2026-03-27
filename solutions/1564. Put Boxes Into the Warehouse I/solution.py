# Problem: Put Boxes Into the Warehouse I
# Language: python3
# Runtime: 624 ms
# Memory: 33.4 MB

class Solution:
    def maxBoxesInWarehouse(self, A: List[int], W: List[int]) -> int:
        A.sort()
        C = []
        m = inf
        for a in W:
            m = min(m,a)
            C.append(m)
        C = C[::-1]
        
        N1 = len(A)
        N2 = len(W)
        ans = i = j = 0
        while i < N1 and j < N2:
            if A[i] <= C[j]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return ans