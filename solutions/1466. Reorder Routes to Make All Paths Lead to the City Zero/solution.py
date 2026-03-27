# Problem: Reorder Routes to Make All Paths Lead to the City Zero
# Language: python3
# Runtime: 988 ms
# Memory: 39.9 MB

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        roads = set()
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
            roads.add((u,v))
            
        count = 0
        def dfs(node, visited):
            nonlocal count            
            for parent in graph[node]:
                if parent not in visited:
                    if (parent, node) not in roads:
                        count += 1
                    dfs(parent, visited | {node})
                    
                    
            
        dfs(0, set())
        return count
        