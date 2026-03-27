# Problem: Maximum Segment Sum After Removals
# Language: python3
# Runtime: 2191 ms
# Memory: 68.2 MB

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
           UF.setdefault(x,x)
           UF.setdefault(y,y)
           UF[find(x)] = find(y)
        
        S = {}
        N = len(nums)
        ans = []
        mx = 0
        for q in removeQueries[::-1]:
            ans.append(mx)
            union(q,q)
            
            sL = 0
            if q > 0 and q - 1 in UF:                
                pl = find(q-1)
                sL = S[pl]
                union(q,q-1)
                
            sR = 0
            if q < N-1 and q + 1 in UF:
                pr = find(q+1)
                sR = S[pr]
                union(q,q+1)
            
            s = sL + nums[q] + sR
            S[find(q)] = s
            
            mx = max(s, mx)
        return ans[::-1]
            
        