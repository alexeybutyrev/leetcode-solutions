# Problem: Furthest Building You Can Reach
# Language: python3
# Runtime: 398 ms
# Memory: 31.1 MB

class Solution:
    def furthestBuilding(self, A: List[int], B: int, L: int) -> int:
        N = len(A)
        
        h = []
        
        for i in range(1,N):
            delta = A[i] - A[i-1]
            if delta > 0:
                if L:
                    heappush(h,delta)
                    L-=1
                else:
                    if h:
                        if h[0] >= delta:
                            if B >= delta:
                                B-=delta
                            else:
                                return i - 1
                        else:
                            d2 = heappop(h)
                            heappush(h,delta)
                            if B >= d2:
                                B -= d2
                            else:
                                return i-1
                    else:
                        if B >= delta:
                            B -= delta
                        else:
                            return i - 1
            
        return N - 1