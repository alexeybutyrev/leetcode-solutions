# Problem: Maximum Value of an Ordered Triplet I
# Language: python3
# Runtime: 224 ms
# Memory: 16.3 MB

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])
        return ans