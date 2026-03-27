# Problem: Count of Smaller Numbers After Self
# Language: python3
# Runtime: 627 ms
# Memory: 36 MB

from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        A = SortedList()
        ans = []
        for x in nums:
            ind = A.bisect_left(x)
            ans.append(ind)
            A.add(x)
        return ans[::-1]
