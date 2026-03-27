# Problem: Minimum Operations to Exceed Threshold Value I
# Language: python3
# Runtime: 63 ms
# Memory: 17 MB

from sortedcontainers import SortedList
class Solution:
    def minOperations(self, l: List[int], k: int) -> int:
        A = SortedList()
        for x in l:
            A.add(x)
        
        ans = 0
        while A and A[0] < k:
            x = A.pop(0)
            ans += 1
        return ans