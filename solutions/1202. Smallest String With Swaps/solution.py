# Problem: Smallest String With Swaps
# Language: python3
# Runtime: 829 ms
# Memory: 79.3 MB

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        A = list(s)
        
        N = len(s)
        
        ans = [''] * N
        
        graph = defaultdict(list)
        inds = set()
        for u,v in pairs:
            inds.add(u)
            inds.add(v)
            graph[u].append(v)
            graph[v].append(u)
        
        global_seen = set()
        
        def dfs(u):
            seen.add(u)
            for v in graph[u]:
                if v not in seen:
                    dfs(v)
        
        for i in inds:
            if i not in global_seen:
                seen = set()
                dfs(i)
                global_seen |= seen
                L = [s[u] for u in seen]
                L.sort()
                for k,j in enumerate(sorted(seen)):
                    ans[j] = L[k]
        #print(ans)
        for i,l in enumerate(ans):
            if not l:
                ans[i] = s[i]
        
        return "".join(ans)
            
        
            