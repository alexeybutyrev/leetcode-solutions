# Problem: Smallest Number in Infinite Set
# Language: python3
# Runtime: 147 ms
# Memory: 14.7 MB

class SmallestInfiniteSet:

    def __init__(self):
        self.s = set(range(1,1001))
        self.h = []
        for x in range(1,1001):
            heappush(self.h,x)
        

    def popSmallest(self) -> int:
        x = heappop(self.h)
        self.s.remove(x)
        return x

    def addBack(self, num: int) -> None:
        if num not in self.s:
            self.s.add(num)
            heappush(self.h, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)