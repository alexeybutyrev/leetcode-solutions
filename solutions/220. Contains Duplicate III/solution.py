# Problem: Contains Duplicate III
# Language: python3
# Runtime: 356 ms
# Memory: 17.3 MB

from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, A: List[int], k: int, t: int) -> bool:
        s = SortedList()
        for i,a in enumerate(A):
            if len(s) == k+1:
                s.remove(A[i-k-1])
                
            left  = s.bisect_left(a - t)
            right = s.bisect_right(a + t)
            if left != right:
                return True
            s.add(a)
        return False