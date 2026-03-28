# Problem: Stock Price Fluctuation 
# Language: python3
# Runtime: 932 ms
# Memory: 56.7 MB

from sortedcontainers import SortedList
class StockPrice:

    def __init__(self):
        self.stock = {}
        self.mts = -1
        self.sl = SortedList()
        
    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.stock:
            self.sl.add(price)
        else:
            
            self.sl.remove(self.stock[timestamp])
            self.sl.add(price)
            
        self.stock[timestamp] = price
        self.mts = max(self.mts, timestamp)
        
    def current(self) -> int:
        return self.stock[self.mts]

    def maximum(self) -> int:
        return self.sl[-1]

    def minimum(self) -> int:
        return self.sl[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()