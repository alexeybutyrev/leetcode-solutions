# Problem: Minimize Max Distance to Gas Station
# Language: python3
# Runtime: 714 ms
# Memory: 14.9 MB

class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        
        def possible(D):
            count = 0
            for a,b in zip(stations, stations[1:]):
                count += int((b - a) / D)
                if count > K:
                    return True
            return False
        lo = 0
        hi = max(b - a for a,b in zip(stations, stations[1:]))
        while abs(lo - hi) > 1e-6:
            mid = (hi + lo) * 0.5
            if possible(mid):
                lo = mid
            else:
                hi = mid
        
        return lo
                
        