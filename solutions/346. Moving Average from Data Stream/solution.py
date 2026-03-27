# Problem: Moving Average from Data Stream
# Language: python3
# Runtime: 86 ms
# Memory: 19.5 MB

class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.N = size
        

    def next(self, val: int) -> float:
        self.q.append(val)
        if len(self.q) > self.N:
            self.q.popleft()
        return sum(self.q) / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)