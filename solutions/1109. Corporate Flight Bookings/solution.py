# Problem: Corporate Flight Bookings
# Language: python3
# Runtime: 856 ms
# Memory: 28.6 MB

from collections import deque
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n+1)
        
        for i, j, k in bookings:
            ans[i-1] += k
            ans[j] -= k
        
        for i in range(1,n):
            ans[i] += ans[i-1]
        return ans[:-1]