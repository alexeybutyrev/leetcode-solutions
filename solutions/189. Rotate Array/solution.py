# Problem: Rotate Array
# Language: python3
# Runtime: 292 ms
# Memory: 26 MB

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k %= N
        
        for i in range(N-k):
            nums.append(nums[i])
        
        for i in range(N):
            nums[i] = nums[N-k+i]
        
        for i in range(N-k):
            nums.pop()
        