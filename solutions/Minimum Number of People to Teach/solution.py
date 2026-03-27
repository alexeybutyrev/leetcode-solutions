# Problem: Minimum Number of People to Teach
# Language: python3
# Runtime: 2284 ms
# Memory: 32.3 MB

class Solution:
    def minimumTeachings(self, n: int, L: List[List[int]], g: List[List[int]]) -> int:
        
        
        graph = []
        M = len(L)
        langs = set()
        LNGS = defaultdict(set)
        for i in range(M):
            LNGS[i] = set(L[i])
            langs |= LNGS[i]

        for u,v in g:
            u -=1
            v -=1
            if not (LNGS[u] & LNGS[v]):
                graph.append((u,v))
                graph.append((v,u))

        ans = M
        for l in langs:
            teach = [False] * M
            for u,v in graph:
                if l in LNGS[u] & LNGS[v]: continue

                if l in LNGS[u]:
                    LNGS[v].add(l)
                    teach[v] = True
                else:
                    LNGS[u].add(l)
                    teach[u] = True
            ans = min(ans, sum(teach))
        
        return ans
