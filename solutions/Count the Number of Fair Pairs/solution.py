# Problem: Count the Number of Fair Pairs
# Language: python3
# Runtime: 732 ms
# Memory: 32.5 MB

from sortedcontainers import SortedList
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        A = SortedList()
        ans = 0
        for a in nums:
            l = A.bisect_left(lower- a)
            r = A.bisect_right(upper-a)
            ans += r - l
            A.add(a)
        return ans