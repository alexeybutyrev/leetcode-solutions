# Problem: Shuffle an Array
# Language: python3
# Runtime: 320 ms
# Memory: 19.6 MB

from random import sample
class Solution:

    def __init__(self, nums: List[int]):
        self.A = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.A

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        rnd = []
        for i in sample(range(len(self.A)), len(self.A)):
            rnd.append(self.A[i])
        return rnd


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()