# Problem: Flatten 2D Vector
# Language: python3
# Runtime: 140 ms
# Memory: 19.3 MB

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.A = []
        for v in vec:
            self.A.extend(v)
        self.N = len(self.A)
        self.curr = 0

    def next(self) -> int:
        x = self.A[self.curr]
        self.curr += 1
        return x

    def hasNext(self) -> bool:
        return self.curr < self.N


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()