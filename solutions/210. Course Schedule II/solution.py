# Problem: Course Schedule II
# Language: python3
# Runtime: 114 ms
# Memory: 15.6 MB

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        c = Counter()
        for v,u in prerequisites:
            graph[u].append(v)
            c[v] += 1
        
        
        q = []
        seen = set()
        ans = []
        for i in range(n):
            if not c[i]:
                q.append(i)
                ans.append(i)
                seen.add(i)
        
        
        for node in q:
            for nb in graph[node]:
                c[nb] -= 1
                if not c[nb]:
                    q.append(nb)
                    ans.append(nb)
                    seen.add(nb)
        
        return ans if len(seen) == n else []