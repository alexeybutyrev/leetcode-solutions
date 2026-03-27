# Problem: Find XOR Sum of All Pairs Bitwise AND
# Language: python3
# Runtime: 968 ms
# Memory: 30.5 MB

class Solution:
    def getXORSum(self, A: List[int], B: List[int]) -> int:
        
        ans1 = 0
        for a in A:
            ans1 ^= a
        ans2 = 0
        for b in B:
            ans2 ^= b
        
            
        
        return ans1 & ans2
        