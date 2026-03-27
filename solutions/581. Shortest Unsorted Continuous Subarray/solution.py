# Problem: Shortest Unsorted Continuous Subarray
# Language: python3
# Runtime: 216 ms
# Memory: 15.5 MB

class Solution:
    def findUnsortedSubarray(self, A: List[int]) -> int:
        N = len(A)
        B = sorted(A)
        s = N 
        e = 0
        for i in range(N):
            if A[i] != B[i]:
                s = min(s,i)
                e = max(e,i)
        
        return e - s + 1 if e >= s else 0