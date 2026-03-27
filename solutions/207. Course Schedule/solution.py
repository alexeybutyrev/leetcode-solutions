# Problem: Course Schedule
# Language: python3
# Runtime: 128 ms
# Memory: 15.7 MB

class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        c = Counter()
        for v,u in prerequisites:
            graph[u].append(v)
            c[v] += 1
        
        
        q = []
        seen = set()
        for i in range(n):
            if not c[i]:
                q.append(i)
                seen.add(i)
        
        
        for node in q:
            for nb in graph[node]:
                c[nb] -= 1
                if not c[nb]:
                    q.append(nb)
                    seen.add(nb)
        
        return len(seen) == n
                    
                