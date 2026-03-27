# Problem: Maximum Length of Subarray With Positive Product
# Language: python3
# Runtime: 704 ms
# Memory: 29.2 MB

class Solution:
    def getMaxLen(self, A: List[int]) -> int:
        
        def count(A):
            N = len(A)
            np = 1 if A[0] > 0 else 0
            nn = 1 if A[0] < 0 else 0

            ans = np
            for i in range(1,N):
                if A[i] > 0:
                    np += 1
                elif A[i] < 0:
                    nn += 1
                else:
                    np = nn = 0
                if nn % 2 == 0:
                    ans = max(ans, np + nn)
            return ans
        return max(count(A), count(A[::-1]))

      