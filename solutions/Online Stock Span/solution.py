# Problem: Online Stock Span
# Language: python3
# Runtime: 428 ms
# Memory: 19.1 MB


class StockSpanner:
    
    def __init__(self):
        self.stack = []
        
        

    def next(self, price: int) -> int:
        weight = 1
        
        while self.stack and self.stack[-1][0] <= price:
            p, w = self.stack.pop()
            weight += w
            
        self.stack.append((price, weight))
        return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)