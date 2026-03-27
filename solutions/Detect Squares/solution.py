# Problem: Detect Squares
# Language: python3
# Runtime: 2060 ms
# Memory: 17 MB

class DetectSquares:

    def __init__(self):
        self.DX = defaultdict(Counter)
        self.DY = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.DX[x][y] += 1
        self.DY[y][x] += 1
        

    def count(self, point: List[int]) -> int:
        x0,y0 = point
        c0 = 1
        ans = 0
        for cx in self.DY[y0]:
            if cx != x0:
                a = abs(cx - x0)
                n = self.DY[y0][cx]
                ans += n * self.DX[cx][y0-a] * self.DX[x0][y0-a]
                ans += n * self.DX[cx][y0+a] * self.DX[x0][y0+a]
        return ans * c0
            
            


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)