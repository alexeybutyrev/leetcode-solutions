# Problem: Random Pick Index
# Language: python3
# Runtime: 296 ms
# Memory: 17.9 MB

from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.inds = {}

    def pick(self, target: int) -> int:
        
        if target not in self.inds:
            n = len(self.nums)
            self.inds[target] = []


            for i in range(n):

                if self.nums[i] == target:
                    self.inds[target].append(i)


        ind = randint(0, len(self.inds[target])-1)
        
        return self.inds[target][ind]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)