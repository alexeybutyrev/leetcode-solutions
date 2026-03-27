# Problem: Sliding Window Median
# Language: python3
# Runtime: 623 ms
# Memory: 27.1 MB

from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, A: List[int], k: int) -> List[float]:
        q = SortedList()
        ans = []
        for i,a in enumerate(A):
            
            if len(q) == k:
                q.remove(A[i-k])
            q.add(a)
            
            if len(q) == k:
                x = q[k//2] if k & 1 else (q[k//2] + q[k//2 -1]) * 0.5
                ans.append(x)
            
        return ans