# Problem: Minimum One Bit Operations to Make Integers Zero
# Language: python3
# Runtime: 0 ms
# Memory: 17.9 MB

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        k = 0
        mask = 1
        
        while mask <= n:
            if n & mask:
                ans = 2 ** (k + 1) - 1 - ans
                
            mask <<= 1
            k += 1
        
        return ans
                        