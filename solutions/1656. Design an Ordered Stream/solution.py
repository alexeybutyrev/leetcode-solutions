# Problem: Design an Ordered Stream
# Language: python3
# Runtime: 212 ms
# Memory: 14.9 MB

class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.pointer = 0
        self.container = [None] * n

    def insert(self, id: int, value: str) -> List[str]:
        self.container[id-1] = value
        if id-1 > self.pointer:
            return []
        
        res = []
        while self.pointer < self.n and self.container[self.pointer] is not None:
            res.append(self.container[self.pointer])
            self.pointer += 1    
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)