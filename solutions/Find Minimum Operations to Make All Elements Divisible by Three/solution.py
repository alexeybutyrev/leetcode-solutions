# Problem: Find Minimum Operations to Make All Elements Divisible by Three
# Language: python3
# Runtime: 0 ms
# Memory: 17.7 MB

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if x % 3 == 0: continue
            
            if (x - 1) % 3 == 0 or (x + 1) % 3 == 0:
                ans +=1
            else:
                ans += 2
        return ans