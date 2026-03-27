# Problem: Maximum Score of a Node Sequence
# Language: python3
# Runtime: 3027 ms
# Memory: 38.9 MB

class Solution:
    def maximumScore(self, S: List[int], edges: List[List[int]]) -> int:
        L = 4
        
        graph = defaultdict(list)
        for i,(u,v) in enumerate(edges):
            graph[u].append(v)
            graph[v].append(u)
        
        
        for u in graph:
            graph[u].sort(key = lambda x: S[x], reverse = True)
            graph[u] = graph[u][:4]
        
        ans = -1
        for u,v in edges:
            for w in graph[u]:
                for l in graph[v]:
                    if len(set([u,v,w,l])) == 4:
                        ans = max(ans, S[u] + S[v] + S[w] + S[l])
        return ans
        
        
            
        
                