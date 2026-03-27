# Problem: Count the Number of Good Nodes
# Language: python3
# Runtime: 2971 ms
# Memory: 101.4 MB

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        self.ans = 0
        def walk(node,p):
            if len(graph[node]) == 1 and p == graph[node][0]:
                self.ans += 1
                return 1
            
            s = 0
            seen = set()
            b = -1
            for v in graph[node]:
                
                if v != p:
                    a = walk(v,node)                    
                    s += a
                    seen.add(a)
            if len(seen) == 1:
                self.ans += 1
            return s + 1


        walk(0,-1)
        return self.ans