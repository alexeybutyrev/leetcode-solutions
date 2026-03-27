# Problem: Minimum Number of Operations to Make Array XOR Equal to K
# Language: python3
# Runtime: 590 ms
# Memory: 31.7 MB

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = 0
        for a in nums:
            x ^= a
        
        ans = 0
        for i in range(32):
            if (k & 1 <<i) != (x & 1 <<i):
                ans += 1
        return ans
                