# Problem: Similar String Groups
# Language: python3
# Runtime: 303 ms
# Memory: 14.4 MB

class Solution:
    def numSimilarGroups(self, W: List[str]) -> int:
        def is_sim(w1,w2):
            c = 0
            for l1,l2 in zip(w1,w2):
                if l1 != l2:
                    c += 1
                    if c > 2:
                        return False
            return True
            
        #W = [list(w) for w in W]
        N = len(W)
        L = len(W[0])
        
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        for i in range(N):
            union(i,i)
            

        for i in range(N):
            for j in range(i+1,N):
                if is_sim(W[i],W[j]):
                    union(i,j)
                
        return len({find(i) for i in range(N)})