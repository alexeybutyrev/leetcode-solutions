# Problem: Average Waiting Time
# Language: python3
# Runtime: 731 ms
# Memory: 57.2 MB

class Solution:
    def averageWaitingTime(self, A: List[List[int]]) -> float:
        T = A[0][0]
        s = A[0][1]
        T += s
        for t,d in A[1:]:
            if T > t:
                dd = T-t
                s += dd + d
                T += d
            else:
                s += d
                T = t + d
        return s /len(A)
            