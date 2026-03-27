# Problem: Find Median from Data Stream
# Language: python3
# Runtime: 452 ms
# Memory: 26.2 MB

from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = SortedList()

    def addNum(self, num: int) -> None:
        self.A.add(num)

    def findMedian(self) -> float:
        N = len(self.A)
        if N & 1:
            return self.A[N//2]
        return (self.A[N//2-1] + self.A[N//2]) * 0.5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()