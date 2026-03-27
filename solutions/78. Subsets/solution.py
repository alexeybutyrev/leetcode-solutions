# Problem: Subsets
# Language: python3
# Runtime: 28 ms
# Memory: 14.5 MB

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        S = {tuple(nums)}
        
        ans = set(tuple())
        while S:
            ans |= S
            S = { l[:i] + l[i+1:]  for l in S for i in range(len(l))}
        
        
        return ans