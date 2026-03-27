# Problem: Reverse Pairs
# Language: python3
# Runtime: 521 ms
# Memory: 23.4 MB

from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, A: List[int]) -> int:
        L = SortedList()
        ans = 0
        while A:
            x = A.pop()
            ind = L.bisect_left(x)
            ans += ind
            L.add(2 * x)
        return ans