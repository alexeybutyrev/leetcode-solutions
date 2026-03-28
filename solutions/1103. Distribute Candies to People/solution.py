# Problem: Distribute Candies to People
# Language: python3
# Runtime: 40 ms
# Memory: 14.2 MB

class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:

        
        c0 = 0
        ans = [0] * n
        while candies:
            for i in range(n):
                c0 += 1
                if candies <= c0:
                    ans[i] += candies
                    return ans
                ans[i] += c0
                candies -= c0
        
        
        return ans
            