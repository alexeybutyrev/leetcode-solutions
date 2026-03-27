# Problem: Implement Router
# Language: python3
# Runtime: 505 ms
# Memory: 91.1 MB

class Router:

    def __init__(self, L: int):
        self.L = L
        self.d = defaultdict(deque)
        self.q = deque()
        self.seen = set()
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination,timestamp) in self.seen:
            return False
        if len(self.q) == self.L:
            s,d,t = self.forwardPacket()
        self.q.append((source,destination,timestamp))
        self.d[destination].append(timestamp)
        self.seen.add((source,destination,timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if self.q:
            s,d,t = self.q.popleft()
            self.d[d].popleft()
            self.seen.remove((s,d,t))
            return [s,d,t]
        return []

    def getCount(self, d: int, sT: int, eT: int) -> int:
        L = bisect_left(self.d[d], sT)
        R = bisect_right(self.d[d], eT)
        return R - L


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)