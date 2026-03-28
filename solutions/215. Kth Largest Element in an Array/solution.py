# Problem: Kth Largest Element in an Array
# Language: python3
# Runtime: 56 ms
# Memory: 14.6 MB

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]