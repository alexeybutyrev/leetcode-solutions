# Problem: Bus Routes
# Language: python3
# Runtime: 1310 ms
# Memory: 48.3 MB

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        line = defaultdict(set)
        for j,r in enumerate(routes):
            for x in r:
                line[x].add(j)
        
        seen = set()
        count = 1
        q = deque()
        for s in line[source]:
            q += routes[s]
            seen.add(s)

        while q:
            L = len(q)
            for _ in range(L):
                node = q.popleft()
                if node == target:
                    return count
                for x in line[node]:
                    if x not in seen:
                        seen.add(x)
                        q += routes[x]
            count += 1
        return -1
        
