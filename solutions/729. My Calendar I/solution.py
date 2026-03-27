# Problem: My Calendar I
# Language: python3
# Runtime: 251 ms
# Memory: 15.2 MB

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
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)