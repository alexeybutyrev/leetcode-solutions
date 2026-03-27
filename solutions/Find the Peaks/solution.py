# Problem: Find the Peaks
# Language: python3
# Runtime: 56 ms
# Memory: 16.3 MB

class Solution:
    def findPeaks(self, A: List[int]) -> List[int]:
        ans = []
        for i in range(1,len(A) -1):
            if A[i-1] < A[i] > A[i+1]:
                ans.append(i)
        return ans