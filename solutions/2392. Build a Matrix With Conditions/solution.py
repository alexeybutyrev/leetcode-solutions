# Problem: Build a Matrix With Conditions
# Language: python3
# Runtime: 633 ms
# Memory: 26.4 MB

def returnOrder(n,prerequisites):
    graph = defaultdict(set)
    c = Counter()
    pairs = set()
    for v,u in prerequisites:
        if (v,u) not in pairs:
            graph[u].add(v)
            c[v] += 1
        pairs.add((v,u))


    q = []
    seen = set()
    ans = []
    for i in range(1,n+1):
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
    
class Solution:
    def buildMatrix(self, K: int, RC: List[List[int]], CC: List[List[int]]) -> List[List[int]]:
        ANS =[[0] * K for _ in range(K)]
        
        minR = defaultdict(lambda : 0)
        minC = defaultdict(lambda : K-1)
        
        maxR = defaultdict(lambda : K-1)
        maxC = defaultdict(lambda : 0)
        
        nums = set()
        graphR = defaultdict(set)
        
        A = returnOrder(K,RC)[::-1]
        B = returnOrder(K,CC)[::-1]

        if not A:
            return []
        
        if not B:
            return []
        
        x = {i+1:i for i in range(K)}
        y = {i+1:i for i in range(K)}
        
        for k in range(1,K+1):
            
            if k in A:
                I = A.index(k)
                x[k] = I
            if k in B:
                J = B.index(k)
                y[k] = J
        
        for k in range(1,K+1):
            ANS[x[k]][y[k]] = k
            
        return ANS
        
        
            
            
        
        