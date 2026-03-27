# Problem: Number of Arithmetic Triplets
# Language: python3
# Runtime: 3212 ms
# Memory: 13.9 MB

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    if nums[j] - nums[i] == nums[k] - nums[j] == diff:
                        ans +=1
        return ans