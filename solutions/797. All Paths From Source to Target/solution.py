# Problem: All Paths From Source to Target
# Language: python3
# Runtime: 108 ms
# Memory: 16 MB

from collections import defaultdict, deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        g = defaultdict()
        for u,l in enumerate(graph):
            g[u] = l
        
        n = len(graph)
        
        q = deque()
        q.append((0,[]))
        res = []
        while q:
            l = len(q)
            for _ in range(l):
                #print(q, q.popleft())
                node, seq = q.popleft()
                if node == n - 1:
                    res.append(seq + [n-1])
                else:
                    for nd in g[node]:
                        q.append((nd, seq + [node]))
                        
        return res