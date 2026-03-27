# Problem: Split Array into Consecutive Subsequences
# Language: python3
# Runtime: 705 ms
# Memory: 15.4 MB

class Solution:
    def isPossible(self, A: List[int]) -> bool:
        hm = {}
        
        for x in A:
            #print(x,hm)
            if x-1 in hm:
                c = heappop(hm[x-1])
                if not hm[x-1]: del hm[x-1]
                if x not in hm: hm[x] = []
                heappush(hm[x],c+1)
                
            else:
                if x not in hm:
                    hm[x] = []
                heappush(hm[x],1)
        for x in hm:
            c = heappop(hm[x])
            if c < 3:
                return False
        return True
        