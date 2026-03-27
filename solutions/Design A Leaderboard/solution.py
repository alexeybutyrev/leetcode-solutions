# Problem: Design A Leaderboard
# Language: python3
# Runtime: 87 ms
# Memory: 16.9 MB

from sortedcontainers import SortedList
class Leaderboard:

    def __init__(self):
        self.A = SortedList()
        self.hm = {}

    def addScore(self, pid: int, score: int) -> None:
        if pid not in self.hm:
            self.hm[pid] = score
            
        else:
            s = self.hm[pid]
            self.A.remove((s,pid))
            score = s + score
            self.hm[pid] = score
        self.A.add((score, pid))
        
        

    def top(self, K: int) -> int:
        count = s = 0
        for j in range(len(self.A) - 1, -1,-1):
            count += 1
            s += self.A[j][0]
            if count == K: break
            
        return s

    def reset(self, pid: int) -> None:
        if pid in self.hm:
            s = self.hm[pid]
            self.A.remove((s,pid))
            del self.hm[pid]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)