# Problem: Construct String With Repeat Limit
# Language: python3
# Runtime: 716 ms
# Memory: 15.8 MB

class Solution:
    def repeatLimitedString(self, s: str, K: int) -> str:
        c = Counter(s)
        h = []
        for k,v in c.items():
            heappush(h, ( (-ord(k),k,v)))
        
        ans = ""
        K2 = 1
        while len(h) > 1:
            o1,k1,v1 = heappop(h)
            
            if v1 > K:
                ans += k1 * K
                h2 = []
                
                heappush(h2, ( (o1,k1,v1-K)))
                
                if h:
                    o2,k2,v2 = heappop(h)
                    if v2 > K2:
                        ans += k2 * K2
                        heappush(h, ( (o2,k2,v2-K2)))
                    else:
                        ans += k2 * v2
                    while h:
                        heappush(h2,heappop(h))
                    
                    h = h2
                else:
                    return ans
                
            else:
                ans += k1 * v1
            
            
        if h:
            o1,k1,v1 = heappop(h)
            ans += k1 * min(v1, K)
            
        
        return ans
                    
            

        