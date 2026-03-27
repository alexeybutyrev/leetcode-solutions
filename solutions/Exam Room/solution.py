# Problem: Exam Room
# Language: python3
# Runtime: 212 ms
# Memory: 14.3 MB

class ExamRoom:

    def __init__(self, n: int):
        self.N, self.L = n, []
        
    def seat(self) -> int:
        N, L = self.N, self.L
        if not L: res = 0
        else:
            d, res = L[0], 0
            for a, b in zip(L, L[1:]):
                if (b - a) // 2 > d:
                    d, res = (b - a) // 2, (b + a) // 2
            if N - 1 - L[-1] > d: res = N - 1
        bisect.insort(L, res)
        return res

    def leave(self, p: int) -> None:
        self.L.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)