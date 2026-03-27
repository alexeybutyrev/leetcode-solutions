# Problem: Largest Color Value in a Directed Graph
# Language: python3
# Runtime: 2333 ms
# Memory: 101.4 MB

class Solution:
    def largestPathValue(self, C: str, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        inbound = Counter()
        for u,v in edges:
            graph[u].add(v)
            inbound[v] += 1
        
        q = []
        for node in range(len(C)):
            if inbound[node] == 0:
                q.append(node)
        
        lengths = [[0] * 26 for _ in range(len(C))]
        for node in q:
            lengths[node][ord(C[node]) - ord('a')] += 1
            for nb in graph[node]:
                inbound[nb] -= 1
                for i in range(26):
                    lengths[nb][i] = max(lengths[nb][i], lengths[node][i])
                if inbound[nb] == 0:
                    q.append(nb)
        
        return max(v2  for node in lengths for v2 in node) if sum(inbound.values()) == 0 else -1