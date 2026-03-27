# Problem: Minimum Cost of Buying Candies With Discount
# Language: python3
# Runtime: 36 ms
# Memory: 14.3 MB

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        s = 0
        for i in range(len(cost)):
            if (i+1) % 3 == 0:
                continue
            else:
                s += cost[i]
        return s
        #for i in range():
            