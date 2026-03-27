# Problem: Contiguous Array
# Language: python3
# Runtime: 615 ms
# Memory: 22.1 MB

class Solution:
    def findMaxLength(self, A: List[int]) -> int:
        hm = {0: -1}
        
        x = ans = 0
        for i,a in enumerate(A):
            x += 1 if a else -1 
            if x in hm:
                ans = max(ans, i - hm[x])
            else:
                hm[x] = i
        
        return ans
        