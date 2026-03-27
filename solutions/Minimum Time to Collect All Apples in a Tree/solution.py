# Problem: Minimum Time to Collect All Apples in a Tree
# Language: python3
# Runtime: 658 ms
# Memory: 51.7 MB

import collections
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        hasApple[0], degree = True, [0] * n
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        queue = deque(v for v in range(n) if degree[v] == 1)
        while queue:
            u = queue.popleft()
            if hasApple[u]: continue
            for v in graph[u]:
                if degree[v] > 0:
                    degree[v] -= 1
                    degree[u] -= 1
                    if degree[v] == 1:
                        queue.append(v)
        return sum(degree)