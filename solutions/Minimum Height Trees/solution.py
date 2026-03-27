# Problem: Minimum Height Trees
# Language: python3
# Runtime: 220 ms
# Memory: 18.8 MB

from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if 1 == n:
            return [0]
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = []
        
        for u in graph:
            if len(graph[u]) == 1:
                leaves.append(u)
            
        rem_nodes = n
        
        while rem_nodes > 2:
            rem_nodes -= len(leaves)
            
            new_leaves  = []
            while leaves:
                lf = leaves.pop()
                for u in graph[lf]:
                    graph[u].remove(lf)
                    if len(graph[u]) == 1:
                        new_leaves.append(u)
            leaves = new_leaves
            
        return leaves
