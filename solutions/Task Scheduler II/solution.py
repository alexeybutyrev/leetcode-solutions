# Problem: Task Scheduler II
# Language: python3
# Runtime: 1061 ms
# Memory: 31.3 MB

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        hm = defaultdict(lambda: -inf)
        d = 0
        for a in tasks:
            d = max(d, hm[a] + space + 1)
            hm[a] = d
            d += 1
        
        return d