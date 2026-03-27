# Problem: Design Exam Scores Tracker
# Language: python3
# Runtime: 243 ms
# Memory: 79.3 MB

class ExamTracker:

    def __init__(self):
        self.S = [0]
        self.T = [0]
        self.seen = set()

    def record(self, time: int, score: int) -> None:
        self.S.append(self.S[-1] + score)
        self.T.append(time)
        self.seen.add(time)

    def totalScore(self, startTime: int, endTime: int) -> int:
        inds = bisect_left(self.T,startTime)-1
        inde = bisect_right(self.T,endTime)-1
        # if inds == inde-1 and startTime not in self.seen and endTime not in self.seen: return 0
        return self.S[inde]-self.S[inds]


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)