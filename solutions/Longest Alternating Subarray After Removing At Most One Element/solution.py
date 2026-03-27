# Problem: Longest Alternating Subarray After Removing At Most One Element
# Language: python3
# Runtime: 935 ms
# Memory: 39.3 MB

class Solution:
    def longestAlternating(self, A: List[int]) -> int:
        N = len(A)

        pre1 = [1] * N
        pre2 = [1] * N

        suf1 = [1] * N
        suf2 = [1] * N
        ans = 1
        for i in range(1,N):
            if A[i] > A[i-1]:
                pre1[i] = pre2[i-1] + 1
            if A[i] < A[i-1]:
                pre2[i] = pre1[i-1] + 1
            ans = max(ans, pre1[i], pre2[i])

        for i in range(N-2,-1,-1):
            if A[i] < A[i+1]:
                suf1[i] = suf2[i+1] + 1
            if A[i] > A[i+1]:
                suf2[i] = suf1[i+1] + 1
            ans = max(ans, suf1[i], suf2[i])
        
        for i in range(1,N-1):
            if A[i-1] > A[i+1]:
                ans = max(ans, pre1[i-1] + suf1[i+1])
            
            if A[i-1] < A[i+1]:
                ans = max(ans, pre2[i-1] + suf2[i+1])
        return ans
            
        