# Problem: Fruit Into Baskets
# Language: python3
# Runtime: 840 ms
# Memory: 20.6 MB

class Solution:
    def totalFruit(self, A: List[int]) -> int:
        N = len(A )
        i = 0
        j = 0
        B = {}
        ans = 0
        while j < N and i < N:
            if A[j] not in B and len(B) >= 2:
                while i < j:
                    B[A[i]] -= 1
                    if B[A[i]] == 0:
                        del B[A[i]]
                        i += 1
                        break
                    i += 1
            if A[j] not in B:
                B[A[j]] = 0
            B[A[j]] += 1
            j += 1
            ans = max(ans, j - i)
        
        return ans
            