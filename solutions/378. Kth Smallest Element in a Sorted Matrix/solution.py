# Problem: Kth Smallest Element in a Sorted Matrix
# Language: python3
# Runtime: 489 ms
# Memory: 18.8 MB

class Solution:
    def kthSmallest(self, A: List[List[int]], k: int) -> int:
        n = len(A)

        lo = A[0][0]
        hi = A[-1][-1]
        
        def valid(x):
            count = 0
            for i in range(n):
                for j in range(n):
                    if A[i][j] <= x:
                        count += 1
            return count < k
        
        while lo < hi:
            mid = lo + hi >> 1
            
            if valid(mid):
                lo = mid + 1
            else:
                hi = mid
        
        return lo
        