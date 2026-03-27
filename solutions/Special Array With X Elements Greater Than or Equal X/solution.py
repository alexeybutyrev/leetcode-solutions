# Problem: Special Array With X Elements Greater Than or Equal X
# Language: python3
# Runtime: 39 ms
# Memory: 16.5 MB

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)+1):
            c = 0
            for x in nums:
                if x >= i:
                    c+=1
                if c > i:
                    break
            else:
                if c == i:
                    return i
        return -1