# Problem: Finding MK Average
# Language: python3
# Runtime: 3372 ms
# Memory: 56.3 MB

class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.stream = []
        self.sortedstream = []

    def addElement(self, num: int) -> None:
        self.stream.append(num)
        if len(self.stream)>self.m:
            self.stream.pop(0)

    def calculateMKAverage(self) -> int:
        if len(self.stream)<self.m:
            return -1
        container = sorted(self.stream)[self.k:-self.k]
        return sum(container)//len(container)