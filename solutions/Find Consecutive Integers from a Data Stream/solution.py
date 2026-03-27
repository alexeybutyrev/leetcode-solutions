# Problem: Find Consecutive Integers from a Data Stream
# Language: python3
# Runtime: 591 ms
# Memory: 40 MB

class DataStream:

    def __init__(self, value: int, k: int):
        self.v = value
        self.count = 0
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.v:
            self.count = min(self.count + 1,self.k)
        else:
            self.count = 0
        
        return self.count == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)