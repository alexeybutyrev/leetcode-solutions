# Problem: Special Array With X Elements Greater Than or Equal X
# Language: python3
# Runtime: 60 ms
# Memory: 14.1 MB

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        for i in range(1,101):
            n = len(list((filter(lambda x: x >= i, nums))))
            if n == i:
                return n
        return -1