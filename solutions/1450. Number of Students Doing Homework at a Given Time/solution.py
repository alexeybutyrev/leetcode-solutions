# Problem: Number of Students Doing Homework at a Given Time
# Language: python3
# Runtime: 68 ms
# Memory: 13.8 MB

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        if not startTime:
            return 0
        
        n = len(startTime)
        count = 0
        for i in range(n):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                count +=1
        return count