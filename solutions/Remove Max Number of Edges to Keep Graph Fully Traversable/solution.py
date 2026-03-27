# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable
# Language: python3
# Runtime: 1915 ms
# Memory: 56.2 MB

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        UFA = {}
        def findA(x):
            if UFA[x] != x:
                UFA[x] = findA(UFA[x])
            return UFA[x]
        
        def unionA(x,y):
            UFA.setdefault(x,x)
            UFA.setdefault(y,y)
            UFA[findA(x)] = findA(y)
        
        
        UFB = {}
        def findB(x):
            if UFB[x] != x:
                UFB[x] = findB(UFB[x])
            return UFB[x]
        
        def unionB(x,y):
            UFB.setdefault(x,x)
            UFB.setdefault(y,y)
            UFB[findB(x)] = findB(y)
            
        for i in range(1,n+1):
            unionA(i,i)
            unionB(i,i)
        
        ans = 0
        for c,u,v in edges:
            if c == 3:
                if findA(u) == findA(v) and findB(u) == findB(v):
                    ans += 1
                unionA(u,v)
                unionB(u,v)
        
        for c,u,v in edges:
            if c == 1:
                if findA(u) == findA(v):
                    ans += 1
                unionA(u,v)
        
        for c,u,v in edges:
            if c == 2:
                if findB(u) == findB(v):
                    ans += 1
                unionB(u,v)
                
        sA = set()
        sB = set()
        for i in range(1,n+1):
            sA.add(findA(i))
            sB.add(findB(i))

        if len(sA) != 1 or len(sB) != 1:
            return -1
        
        return ans 