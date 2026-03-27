# Problem: My Calendar I
# Language: python3
# Runtime: 172 ms
# Memory: 17.7 MB

from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.L = SortedList()
        self.R = SortedList()

    def book(self, start: int, end: int) -> bool:
        
        ind = self.L.bisect_left(end)
        
        # check if new interval overlaps with the one before
        if ind and self.R[ind-1] > start: return False
        
        self.L.add(start)
        self.R.add(end)
        return True