# Problem: Max Consecutive Ones III
# Language: python3
# Runtime: 610 ms
# Memory: 17.2 MB

class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        l = 0
        ans = 0
        for r,a in enumerate(A):
            if a == 0:
                k -= 1
            
            while k < 0:
                if A[l] == 0:
                    k+=1
                l += 1
            
            ans = max(ans, r - l+1)
        
        return ans