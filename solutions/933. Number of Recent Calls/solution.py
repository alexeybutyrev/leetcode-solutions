# Problem: Number of Recent Calls
# Language: python3
# Runtime: 288 ms
# Memory: 18.7 MB

from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()
        self.window = 3000
        
    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q and t - self.q[0] > self.window:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)