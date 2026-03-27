# Problem: Minimum K to Reduce Array Within Limit
# Language: python3
# Runtime: 2584 ms
# Memory: 34.5 MB

class Solution:
    def minimumK(self, A: List[int]) -> int:

        def check(k):
            ans = 0
            for x in A:
                ans += ceil(x/k)
            return ans <= k * k


        lo = 1
        hi = max(A) * len(A)

        while lo < hi:
            mid = lo + hi >> 1

            if check(mid):
                hi = mid
            else:
                lo = mid + 1

        
        return lo
            