# Problem: Fancy Sequence
# Language: python3
# Runtime: 219 ms
# Memory: 55.2 MB

class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.a = [1]
        self.b = [0]
        self.X = []

    def append(self, val: int) -> None:
        self.a.append(self.a[-1])
        self.b.append(self.b[-1])
        self.X.append(val)
    
    def quickmul(self, x: int, y: int) -> int:
        return pow(x, y, self.MOD)
    
    # multiplicative inverse
    def inv(self, x: int) -> int:
        return self.quickmul(x, self.MOD - 2)

    def addAll(self, inc: int) -> None:
        self.b[-1] = self.b[-1] + inc

    def multAll(self, m: int) -> None:
        self.a[-1] = self.a[-1] * m % self.MOD
        self.b[-1] = self.b[-1] * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.X): return -1

        ao = self.inv(self.a[idx]) * self.a[-1]
        bo = self.b[-1] - self.b[idx] * ao
        return (ao * self.X[idx] + bo) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)