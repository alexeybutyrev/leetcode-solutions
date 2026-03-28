# Problem: Shortest Subarray to be Removed to Make Array Sorted
# Language: python3
# Runtime: 628 ms
# Memory: 28.7 MB

class Solution:
    def findLengthOfShortestSubarray(self, A: List[int]) -> int:
        # longest array inside
        
        N = len(A)
        l = 0

        
        for l in range(1,N):
            if A[l] < A[l-1]:
                break
        else:
            return 0
        
        ans = N - l
        
        for r in range(N - 2, -1, -1):
            if A[r] > A[r+1]:
                break
        
        ans = min(ans, r + 1)
        j = r + 1
        i = 0
        while i < l and j < N:
            if A[i] <= A[j]:
                ans = min(ans, j - i-1)
                i += 1
            else:
                j += 1
        
        return ans
        
                    
        