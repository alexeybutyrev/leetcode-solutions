# Problem: Total Cost to Hire K Workers
# Language: python3
# Runtime: 879 ms
# Memory: 27.3 MB

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        hL = []
        hR = []
        
        A = deque(costs)
        
        for i in range(candidates):
            if A:
                heappush(hL,A.popleft())
                if A:
                    heappush(hR,A.pop())
                else:
                    break
            else:
                break
        
        ans = 0
        for _ in range(k):
            if hL: 
                xl = heappop(hL)
            else:
                ans += heappop(hR)
                continue
            
            if hR:
                xr = heappop(hR)
                if xl <= xr:
                    if A: heappush(hL, A.popleft())
                    heappush(hR, xr)
                    ans += xl
                else:
                    ans += xr
                    if A: heappush(hR, A.pop())
                    heappush(hL, xl)
            else:
                ans += xl
        return ans