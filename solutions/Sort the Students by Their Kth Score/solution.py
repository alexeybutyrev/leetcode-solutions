# Problem: Sort the Students by Their Kth Score
# Language: python3
# Runtime: 451 ms
# Memory: 20 MB

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key = lambda x: -x[k])
        return score