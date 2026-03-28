# Problem: Remove Boxes
# Language: python3
# Runtime: 756 ms
# Memory: 24.8 MB

from itertools import groupby
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        A = [ (k,len(list(v))) for k,v in groupby(boxes)]
        c = Counter([k for k,_ in A])
        keys   = []
        counts = []
        ans = 0
        for a,count in A:
            if c[a] == 1 and count == 1:
                ans += 1
            else:
                keys.append(a)
                counts.append(count)
        #print(keys, counts)
        N = len(keys)
        
        @functools.lru_cache(None)
        def dfs(i,j,k):
            if i>j: return 0
            cnt=0
            vals = 0
            while (i+cnt)<=j and keys[i]==keys[i+cnt]:
                vals += counts[i+cnt]
                cnt+=1
            i2=i+cnt
            res=dfs(i2,j,0)+(k+vals)**2
            for m in range(i2,j+1):
                if keys[m]==keys[i]:
                    res=max(res, dfs(i2,m-1,0)+dfs(m,j,k+vals))
            return res
        
        #print(ans, dfs(0,N-1,0))
        return ans + dfs(0,N-1,0)
    