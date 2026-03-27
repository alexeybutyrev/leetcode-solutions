# Problem: Sliding Subarray Beauty
# Language: python3
# Runtime: 6440 ms
# Memory: 29 MB

from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        A = SortedList()
        for i in range(k):
            A.add(nums[i])
        ans = [min(A[x-1],0)]
        for i in range(k,len(nums)):
            A.remove(nums[i-k])
            A.add(nums[i])
            ans.append(min(0,A[x-1]))
        return ans