# Problem: Longest Subarray of 1's After Deleting One Element
# Language: python3
# Runtime: 331 ms
# Memory: 19 MB

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        A = [(k,len(list(x))) for k,x in groupby(nums)]
        N = len(A)
        if N == 1:
            return A[0][1] - 1 if A[0][0] else 0
        ans = 0
        for i in range(N):
            if A[i][0]:
                ans = max(ans, A[i][1])
                if i < N - 2 and A[i][0] == A[i+2][0] and A[i+1][1] == 1:
                    ans = max(ans, A[i][1] + A[i+2][1])
        
        return ans
                