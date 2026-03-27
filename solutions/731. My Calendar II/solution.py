# Problem: My Calendar II
# Language: python3
# Runtime: 253 ms
# Memory: 17.5 MB

class MyCalendarTwo:

    def __init__(self):
        self.intervals = []
        self.overlaps  = []
        
    def book(self, start: int, end: int) -> bool:
        for l,r in self.overlaps:
            if start < r and end > l:
                return False
        for l,r in self.intervals:
            if start < r and end > l:
                self.overlaps.append([max(l,start),min(r,end)])
        
        self.intervals.append([start, end])
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)