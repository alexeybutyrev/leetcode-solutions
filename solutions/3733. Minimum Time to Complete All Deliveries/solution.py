# Problem: Minimum Time to Complete All Deliveries
# Language: python3
# Runtime: 15 ms
# Memory: 17.9 MB

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r

        l = r1 * r2 // (gcd(r1,r2))
        def is_valid(t):
            v1 = t - t//r1
            v2 = t - t//r2
            u = t - t //l
            return v1 >= d1 and v2 >= d2 and u >= d1 + d2

        lo = 0
        hi = 10**18 + 1

        while lo < hi:
            mid = lo + hi >> 1
            if is_valid(mid):
                hi = mid
            else:
                lo = mid + 1
                

        return lo