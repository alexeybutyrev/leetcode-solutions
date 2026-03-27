# Problem: Number of Operations to Make Network Connected
# Language: python3
# Runtime: 468 ms
# Memory: 40.9 MB

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        nE = len(connections)
        
        graph = defaultdict(set)
        for u,v in connections:
            graph[u].add(v)
            graph[v].add(u)
            
        visited = set()
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                stack = [i]
                visited.add(i)
                while stack:
                    node = stack.pop()
                    for n in graph[node]:
                        if n not in visited:
                            nE -= 1
                            stack.append(n)
                            visited.add(n)
        print(count, nE)
        return count - 1 if nE >=  count -1 else -1