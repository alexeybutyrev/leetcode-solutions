# Problem: Design Most Recently Used Queue
# Language: python3
# Runtime: 130 ms
# Memory: 17.5 MB

class MRUQueue:

    def __init__(self, n: int):
        self.A = list(range(1,n+1))

    def fetch(self, k: int) -> int:
        x = self.A.pop(k-1)
        self.A.append(x)
        return x


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)