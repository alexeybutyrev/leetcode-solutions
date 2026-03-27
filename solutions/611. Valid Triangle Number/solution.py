# Problem: Valid Triangle Number
# Language: python3
# Runtime: 7123 ms
# Memory: 14.1 MB

class Solution:
    def triangleNumber(self, A: List[int]) -> int:
        # c < a + b
        #A = list(set(A))
        A.sort()
        ans = 0
        for i in range(N:=len(A)-1,0,-1):
            for j in range(i-1,-1,-1):
                k = bisect_right(A[:j],A[i] - A[j])
                ans += j - k
        return ans