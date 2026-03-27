# Problem: Pythagorean Distance Nodes in a Tree
# Language: python3
# Runtime: 933 ms
# Memory: 89.1 MB

class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def walk(x):
            seen = {x}
            d = {}
            d[x] = 0
            q = [x]
            dist = 0
            for u in q:
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
                        d[v] = d[u] + 1
            return d
        X = walk(x)
        Y = walk(y)
        Z = walk(z)
        ans = 0
        for i in range(n):
            
            a,b,c = sorted([X[i], Y[i], Z[i]])
            if a * a + b * b == c * c:
                ans += 1
        
        return ans         