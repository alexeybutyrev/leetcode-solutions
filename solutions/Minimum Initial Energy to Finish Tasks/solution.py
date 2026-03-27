# Problem: Minimum Initial Energy to Finish Tasks
# Language: python3
# Runtime: 1548 ms
# Memory: 59.3 MB

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        tasks.sort(key = lambda x: x[1]-x[0], reverse = True)
        #print(tasks)
        
        start = tasks[0][1]
        delta = start - tasks[0][0]
        
        n = len(tasks)
        
        for i in range(1,n):
            #print(delta, start, tasks[i] )
            if tasks[i][1] > delta:
                start += tasks[i][1] - delta
                delta = tasks[i][1]
                
            delta = delta -  tasks[i][0]
        
        return start