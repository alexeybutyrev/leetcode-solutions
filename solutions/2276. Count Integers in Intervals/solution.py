# Problem: Count Integers in Intervals
# Language: python3
# Runtime: 1367 ms
# Memory: 54.3 MB

from sortedcontainers import SortedList
class CountIntervals:

    def __init__(self):
        self.A = SortedList()
        self.c = 0

    def add(self, left: int, right: int) -> None:
        k = self.A.bisect_left((left, right))
        
        while k < len(self.A) and self.A[k][0] <= right:
            l,r = self.A.pop(k)
            self.c -= r - l + 1
            right = max(right, r)
        
        if k and left <= self.A[k-1][1]:
            l,r = self.A.pop(k-1)
            self.c -= r - l + 1
            right = max(right, r)
            left = l
        self.A.add((left, right))
        self.c += right - left + 1

    def count(self) -> int:
        return self.c


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()