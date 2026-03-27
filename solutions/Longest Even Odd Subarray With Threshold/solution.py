# Problem: Longest Even Odd Subarray With Threshold
# Language: python3
# Runtime: 6779 ms
# Memory: 16.3 MB

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        N = len(nums)
        ans = 0
        for l in range(N):
            if nums[l] % 2 == 0:
                for r in range(l,N):
                    pr = True
                    for i in range(l,r):
                        if nums[i] % 2 == nums[i + 1] % 2:
                            pr = False
                            break
                    if not pr: continue
                        
                    pr = True
                    for i in range(l,r+1):
                        if nums[i] > threshold:
                            pr = False
                            break
                    if pr:
                        ans = max(ans, r-l+1)
        return ans