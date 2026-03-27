# Problem: Maximum XOR for Each Query
# Language: python3
# Runtime: 675 ms
# Memory: 30.3 MB

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        X = 0
        
        for x in nums:
            X ^= x
        
        A = []
        while nums:
            
            
            ans = 0
            for i in range(maximumBit):
                if X & (1 <<i) == 0:
                    ans ^= (1<<i)
            A.append(ans)
            
            n = nums.pop()
            X ^= n
            
        return A