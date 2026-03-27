# Problem: Number of Students Unable to Eat Lunch
# Language: python3
# Runtime: 32 ms
# Memory: 14.4 MB

from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        N = len(students)
        students   =  list(reversed(students))
        sandwiches = list(reversed(sandwiches))
        while N:
            
            for _ in range(N):
                if sandwiches[-1] == students[-1]:
                    sandwiches.pop()
                    students.pop()
                else:
                    s = students.pop()
                    students = [s] + students
            
            if len(students) == N:
                return N
            N = len(students)
        
        return len(students)