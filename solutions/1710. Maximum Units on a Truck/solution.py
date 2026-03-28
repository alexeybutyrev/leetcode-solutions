# Problem: Maximum Units on a Truck
# Language: python3
# Runtime: 148 ms
# Memory: 14.8 MB

class Solution:
    def maximumUnits(self, A: List[List[int]], S: int) -> int:
        A.sort(key = lambda x: x[1])
        ans = 0
        while A and S:
            if A[-1][0] <= S:
                ans += A[-1][0] * A[-1][1]
                S -= A[-1][0]
                A.pop()
            else:
                return ans + A[-1][1] * S
        return ans