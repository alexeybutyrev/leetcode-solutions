# Problem: Parallel Courses III
# Language: python3
# Runtime: 1478 ms
# Memory: 45 MB

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        graph = defaultdict(list)
        c = Counter()
        for u, v in relations:
            u-=1
            v-=1
            graph[u].append(v)
            c[v] += 1
        
        T = [0] * n
        q = deque()
        for node in range(n):
            if c[node] == 0:
                q.append(node)
                T[node] = time[node]
        
        while q:
            L = len(q)
            for _ in range(L):
                u = q.popleft()
                for v in graph[u]:
                    c[v] -= 1
                    T[v] = max(T[u], T[v])
                    if c[v] == 0:
                        q.append(v)
                        T[v] += time[v]
        return max(T)