# Problem: Power Grid Maintenance
# Language: python3
# Runtime: 2621 ms
# Memory: 218.1 MB

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])

            return UF[x]

        

        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        for i in range(1,c+1):
            union(i,i)
        for u,v in connections:
            union(u,v)
        

        D = defaultdict(SortedSet)

        for i in range(1,c+1):
            p = find(i)
            D[p].add(i)
            D[p].add(p)
        
        ans = []
        off = set()
        for s,n in queries:
            p = find(n)
            if s == 2:
                D[p].discard(n)
                continue
            
            if not D[p]:
                ans.append(-1)
                continue
            if n not in D[p]:
                ans.append(D[p][0])
            else:
                ans.append(n)
            
        return ans