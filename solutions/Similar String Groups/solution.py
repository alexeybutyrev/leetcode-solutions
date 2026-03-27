# Problem: Similar String Groups
# Language: python3
# Runtime: 275 ms
# Memory: 17.4 MB

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # checks if two string are the same with one swap
        def check(x,y):
            count = 0
            for a,b in zip(x,y):
                if a != b: 
                    count += 1
                if count > 2: return False
            return True
        
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
            
        N = len(strs)
        for i in range(N):
            union(strs[i],strs[i])
            for j in range(i+1,N):
                if check(strs[i],strs[j]):
                    union(strs[i],strs[j])
        
        return len(set(find(x) for x in strs))