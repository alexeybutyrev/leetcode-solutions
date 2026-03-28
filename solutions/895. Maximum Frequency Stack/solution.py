# Problem: Maximum Frequency Stack
# Language: python3
# Runtime: 296 ms
# Memory: 21.6 MB

from heapq import *
from collections import Counter, defaultdict
class FreqStack:

    def __init__(self):
        self.freq  = Counter()
        self.group = defaultdict(list)
        self.max_freq = 0
        
    def push(self, x: int) -> None:
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.max_freq:
            self.max_freq = f
        self.group[f].append(x)

    def pop(self) -> int:
        num = self.group[self.max_freq].pop()
        self.freq[num] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return num
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()