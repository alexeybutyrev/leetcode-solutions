# Problem: Count Good Triplets in an Array
# Language: python3
# Runtime: 419 ms
# Memory: 43.1 MB

from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, A: List[int], B: List[int]) -> int:
        m = {x:i for i,x in enumerate(A)}
        N = len(A)
        L = SortedList()
        ans = 0
        for x in B:
            ind = m[x]
            left  = L.bisect_left(ind)
            right = (N - ind - 1) - (len(L) - left)
            ans += left * right
            L.add(ind)
        return ans
        