# Problem: Maximum Width Ramp
# Language: python3
# Runtime: 404 ms
# Memory: 27.6 MB

class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        A= [(x,i)for i,x in enumerate(A)]
        A.sort()
        mn = A[0][1]
        ans=0
        for x,i in A[1:]:
            if i < mn:
                mn = i
            else:
                ans = max(ans,i-mn)
        return ans
            