# Problem: Fruit Into Baskets
# Language: python3
# Runtime: 848 ms
# Memory: 20 MB

class Solution:
    def totalFruit(self, A: List[int]) -> int:
        B = {}
        
        N = len(A)
        
        i = 0
        j = 0
        ans = 0
        while i < N and j < N:
            if A[j] not in B:
                B[A[j]] = 1
            else:
                B[A[j]] += 1
            if len(B) > 2:
                while len(B) > 2:
                    B[A[i]] -= 1
                    if not B[A[i]]:
                        del B[A[i]]
                    i += 1
                
            ans = max(ans, 1 + j - i)
            j += 1
            
            
        return ans
            