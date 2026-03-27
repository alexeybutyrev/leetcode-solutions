# Problem: Number of Subarrays That Match a Pattern I
# Language: python3
# Runtime: 61 ms
# Memory: 16.6 MB

class Solution:
    def countMatchingSubarrays(self, A: List[int], P: List[int]) -> int:
        N = len(A)
        M = len(P)
        ans = 0
        for i in range(N-M):
            x = A[i]
            for j in range(M):
                y = A[i+j+1]
                if P[j] == 1:
                    if x >= y: break
                elif P[j] == -1:
                    if x <= y: break
                else:
                    if x != y: break
                x = y
            else:
                ans += 1
        return ans
        