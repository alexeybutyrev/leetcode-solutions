# Problem: Minimum Time to Collect All Apples in a Tree
# Language: python3
# Runtime: 693 ms
# Memory: 54.8 MB

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        hasApple[0] = True
        c = Counter()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            c[u] += 1
            c[v] += 1
        
        q = [u for u in range(n) if c[u] == 1]
        for u in q:
            if hasApple[u]: continue
            for v in graph[u]:
                if c[v]:
                    c[u] -= 1
                    c[v] -= 1
                    if c[v] == 1:
                        q.append(v)
        return sum(c.values())
            