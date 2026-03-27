# Problem: Find if Path Exists in Graph
# Language: python3
# Runtime: 1793 ms
# Memory: 106.3 MB

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        stack = deque([start])
        seen = {start}
        while stack:
            L = len(stack)
            for _ in range(L):
                node = stack.popleft()
                if node == end:
                    return True
                for nbr in graph[node]:
                    if nbr not in seen:
                        seen.add(nbr)
                        stack.append(nbr)
        
        return False
                    