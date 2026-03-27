# Problem: Find the Town Judge
# Language: python3
# Runtime: 1236 ms
# Memory: 19 MB

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        rgraph = defaultdict(list)
        for a,b in trust:
            graph[a].append(b)
            rgraph[b].append(a)
        
        
        for i in range(1,n+1):
            if len(rgraph[i]) == n-1 and not graph[i]:
                return i
        return -1
        