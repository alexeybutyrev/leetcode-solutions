# Problem: Delete Tree Nodes
# Language: python3
# Runtime: 284 ms
# Memory: 40.3 MB

class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        
        graph = defaultdict(set)
        for i in range(nodes):
            if parent[i] > -1:
                graph[parent[i]].add(i)
            else:
                p = i
                
        def dfs(node):
            s = value[node]
            count = 1
            for n in graph[node]:
                (ss,c) = dfs(n)
                s += ss
                count += c
            
            if s == 0:
                return (0,0)
            
            return s, count
        
        return dfs(p)[1]
            
            