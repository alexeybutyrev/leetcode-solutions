# Problem: Number of Orders in the Backlog
# Language: python3
# Runtime: 732 ms
# Memory: 54 MB

from heapq import *
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        B = []
        S = []
        
        maxB = -inf
        minS = inf
        
        for p, count, t in orders:
            if t:
                # sell
                while B and -B[0][0] >= p and count:
                    bp, bc = heappop(B)
                    if bc >= count:
                        bc -= count
                        count = 0
                        if bc:
                            heappush(B, (bp,bc))
                    else:
                        count -= bc
                        
                if count:
                    heappush(S, (p, count))
                    
            else:
                while S and S[0][0] <= p and count:
                    sp, sc = heappop(S)
                    if sc >= count:
                        sc -= count
                        count = 0
                        if sc:
                            heappush(S, (sp,sc))
                    else:
                        count -= sc
                        
                if count:
                    heappush(B, (-p, count))
        
        
        ans = 0
        for _, c in B:
            ans += c
            ans %= MOD
            
        for _, c in S:
            ans += c
            ans %= MOD
        
        return ans % MOD
        