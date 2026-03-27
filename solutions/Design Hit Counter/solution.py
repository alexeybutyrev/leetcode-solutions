# Problem: Design Hit Counter
# Language: python3
# Runtime: 0 ms
# Memory: 19.7 MB

class HitCounter:

    def __init__(self):
        self.A = []

    def hit(self, timestamp: int) -> None:
        self.A.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        return bisect_right(self.A, timestamp) - bisect_right(self.A, timestamp - 300)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)