# Problem: Minimum Recolors to Get K Consecutive Black Blocks
# Language: python3
# Runtime: 0 ms
# Memory: 17.8 MB

class Solution:
    def minimumRecolors(self, A: str, k: int) -> int:
        
        c = Counter(A[:k])
        ans = c["W"]
        
        for j in range(k,len(A)):
            c[A[j-k]] -= 1
            c[A[j]] += 1
            ans = min(ans,c["W"])
        return ans
        