# Problem: Parallel Courses
# Language: python3
# Runtime: 292 ms
# Memory: 18.1 MB

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(set)
        req = defaultdict(set)
        deps = set()
        for u,v in relations:
            graph[u].add(v)
            req[v].add(u)
            deps.add(v)
        
        q = deque()
        visited = set()
        for u in range(1,n+1):
            if u not in deps:
                q.append(u)
                visited.add(u)
        
       # print(graph)
       # print(graph[1])
        count = 0
        learned = set()
        while q:
            #print(q)
            l = len(q)
            count += 1
            learned |= visited
            visited = set()
            for _ in range(l):
                node = q.popleft()
                for k in graph[node]:
                    if k not in learned and len(req[k] & learned) == len(req[k]):
                        q.append(k)
                        visited.add(k)
        learned |= visited
        return count if len(learned) == n else -1