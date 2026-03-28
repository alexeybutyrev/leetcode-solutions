# Problem: Partition to K Equal Sum Subsets
# Language: python3
# Runtime: 1512 ms
# Memory: 14.2 MB

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        n = len(nums)
        if s % k != 0:
            return False
        if k == 1:
            return True
        if n < k:
            return False
        nums.sort(reverse=True)
        target = [s // k] * k
        
        
        def dfs(j):
            if j == n:
                return True
            for i in range(k):
                if target[i] >= nums[j]:
                    target[i] -= nums[j]
                    if dfs(j+1):
                        return True
                    target[i] += nums[j]
            return False
        return dfs(0)
            