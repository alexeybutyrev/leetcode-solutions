# Problem: Number of Ways to Buy Pens and Pencils
# Language: python3
# Runtime: 955 ms
# Memory: 13.8 MB

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost2 < cost1:
            cost2,cost1 = cost1,cost2
        N1 = total // cost1
        count = 0
        for c in range(N1+1):
            N2 = total - cost1*c
            count += N2 // cost2 + 1
        return count