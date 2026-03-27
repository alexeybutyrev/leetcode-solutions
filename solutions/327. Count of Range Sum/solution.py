# Problem: Count of Range Sum
# Language: python3
# Runtime: 1635 ms
# Memory: 31.5 MB

from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lo: int, up: int) -> int:
        A = SortedList()
        s = 0
        ans = 0
        A.add(0)
        for x in nums:
            
            s += x
            l = A.bisect_left(s-up)
            r = A.bisect_right(s-lo)
            ans += r - l
            A.add(s)
        return ans