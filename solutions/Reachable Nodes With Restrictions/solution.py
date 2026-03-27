# Problem: Reachable Nodes With Restrictions
# Language: python3
# Runtime: 2821 ms
# Memory: 72.4 MB

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        R = set(restricted)
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = {0}
        q = [0]
        
        for u in q:
            for v in graph[u]:
                if v not in seen and v not in R:
                    seen.add(v)
                    q.append(v)
        return len(seen)
            