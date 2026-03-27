# Problem: Minimize the Total Price of the Trips
# Language: python3
# Runtime: 279 ms
# Memory: 14.4 MB

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        #find path from node to target
        def walk(node,parent):
            if node == target:
                return [target]
            else:
                for v in graph[node]:
                    if v != parent:
                        x = walk(v,node)
                        if x:
                            return [node] + x
            return None
        
        # count number of node accurances 
        # and total cost for all trips
        c = Counter()
        S = 0
        for u,v in trips:
            target = v
            for x in walk(u,-1):
                c[x] += 1
                S += price[x]
        
        # maximize savings
        @cache
        def dp(node,parent,taken):
            X = 0
            if not taken:
                X = c[node] * (price[node] // 2)
                for v in graph[node]:
                    if v != parent:
                        X += dp(v,node,True)
            a = 0
            for v in graph[node]:
                if v != parent:
                    a += dp(v,node,False)
            return max(X,a)
        
        mx = 0
        for node in range(n):
            mx = max(mx, dp(node, -1,False))
        return S - mx
        
        