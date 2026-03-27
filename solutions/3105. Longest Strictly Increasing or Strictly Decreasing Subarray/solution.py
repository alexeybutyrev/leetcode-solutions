# Problem: Longest Strictly Increasing or Strictly Decreasing Subarray
# Language: python3
# Runtime: 7 ms
# Memory: 17.9 MB

class Solution:
    def longestMonotonicSubarray(self, A: List[int]) -> int:
        ans = 0
        N = len(A)
        for i in range(N):
            l = 1
            for j in range(i+1,N):
                if A[j] > A[j-1]:
                    l += 1
                else:
                    break
            ans = max(ans, l)
        

        for i in range(N):
            l = 1
            for j in range(i+1,N):
                if A[j] < A[j-1]:
                    l += 1
                else:
                    break
            ans = max(ans, l)
        return ans