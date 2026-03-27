# Problem: Maximum Possible Number by Binary Concatenation
# Language: python3
# Runtime: 46 ms
# Memory: 16.5 MB

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        ans = 0
        for x in permutations(nums):
            s = ""
            for y in x:
                s += bin(y)[2:]
                
            ans = max(ans,int(s,2))
        return ans