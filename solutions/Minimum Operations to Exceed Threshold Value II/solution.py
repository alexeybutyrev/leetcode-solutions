# Problem: Minimum Operations to Exceed Threshold Value II
# Language: python3
# Runtime: 1247 ms
# Memory: 39 MB

from sortedcontainers import SortedList
class Solution:
    def minOperations(self, l: List[int], k: int) -> int:
        A = SortedList()
        for x in l:
            A.add(x)
        
        ans = 0
        while A and A[0] < k:
            x = A.pop(0)
            y = A.pop(0)
            
            
            A.add(2*x + y)
            ans += 1
        return ans