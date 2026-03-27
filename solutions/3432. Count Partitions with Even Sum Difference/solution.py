# Problem: Count Partitions with Even Sum Difference
# Language: python3
# Runtime: 3 ms
# Memory: 17.7 MB

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        N = len(nums)
        s1 = ans = 0
        for i in range(N-1):
            s1 += nums[i]
            s2 = 0
            for j in range(i+1,N):
                s2 += nums[j]
            if abs(s1-s2) % 2 == 0:
                ans += 1
        return ans