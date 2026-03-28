# Problem: Task Scheduler
# Language: python3
# Runtime: 540 ms
# Memory: 13.9 MB

from collections import Counter
from heapq import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        h = []
        for k,v in c.items():
            heappush(h,[-v,k])
        
        units = 0
        while h:
            pushback = []
            l = len(h)
            if l >= n+1:
                units += n+1
                for i in range(n+1):
                    e = heappop(h)
                    e[0]+=1
                    if e[0] <0:
                        pushback.append(e)
            else:
                for i in range(l):
                    e = heappop(h)
                    e[0]+=1
                    if e[0] <0:
                        pushback.append(e)
                units += n+1
            for e in pushback:
                heappush(h,e)
                
        return units + l - n-1
        