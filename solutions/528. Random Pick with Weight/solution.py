# Problem: Random Pick with Weight
# Language: python3
# Runtime: 292 ms
# Memory: 18.5 MB

class Solution:

    def __init__(self, w: List[int]):
        self.W = list(accumulate(w))
        self.mx = self.W[-1]
    def pickIndex(self) -> int:
        c = random.randrange(0,self.mx)
        return bisect_right(self.W,c)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()