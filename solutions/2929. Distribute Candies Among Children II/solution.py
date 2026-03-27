# Problem: Distribute Candies Among Children II
# Language: python3
# Runtime: 5790 ms
# Memory: 16.3 MB

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def s(b,a):
            return (b * (b + 1) // 2) - (a * (a + 1) // 2)
        
        limit = min(limit, n)
        
        ans = 0
        for x in range(limit + 1):
            m = n - x
            
            b = min(m,limit)
            a = max(0,m-limit)
            ans += max(b-a+1,0)
            
            #ans += m * (m+1) // 2
            #if m - limit + 1 <= limit+1:
            #    ans += sum(m-limit + 1, limit+1)
        return ans