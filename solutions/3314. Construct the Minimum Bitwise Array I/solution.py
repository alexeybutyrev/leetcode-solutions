# Problem: Construct the Minimum Bitwise Array I
# Language: python3
# Runtime: 183 ms
# Memory: 16.6 MB

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            
            for a in range(1,1001):
                if a | (a+1) == x:
                    ans.append(a)
                    break
            else:
                ans.append(-1)
        return ans