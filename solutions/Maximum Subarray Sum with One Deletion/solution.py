# Problem: Maximum Subarray Sum with One Deletion
# Language: python3
# Runtime: 192 ms
# Memory: 26.3 MB

class Solution:
    def maximumSum(self, A: List[int]) -> int:
        curr = A[0]
        cd = A[0]
        ans = A[0]
        
        for x in A[1:]:
            cd = max(curr, x, cd + x)
            curr = max(x, curr+x)
            ans = max(ans, curr, cd)
        return ans