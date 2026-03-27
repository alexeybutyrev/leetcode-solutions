# Problem: Parallel Courses
# Language: python3
# Runtime: 260 ms
# Memory: 20.9 MB

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        rgraph = defaultdict(list)
        c = Counter()
        for u,v in relations:
            graph[u].append(v)
            rgraph[v].append(u)
            c[v] += 1
        
        q = deque()
        seen = set()
        for i in range(1,n+1):
            if not c[i]:
                q.append(i)
                seen.add(i)
        
        l = 0
        while q:
            L = len(q)
            l += 1
            for _ in range(L):
                u = q.popleft()
                for v in graph[u]:
                    seen.add(v)
                    c[v] -= 1
                    if c[v] == 0:
                        del c[v]
                        q.append(v)
            
        
        return l if len(seen) == n else -1