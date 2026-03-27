# Problem: Minimum Deletions to Make Array Divisible
# Language: python3
# Runtime: 707 ms
# Memory: 33.9 MB

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        s = list(set(numsDivide))
        if len(s) == 1:
            g = s[0]
        else:
            g = gcd(s[0],s[1])
            for x in s[2:]:
                g = gcd(g,x)
        
        m = min(s)
        c = Counter(nums)
        h = []
        ans = 0
        for k,v in c.items():
            heappush(h, (k,v))
            
        while h:
            k,v = heappop(h)
            if k > m:
                return -1
            if g % k == 0:
                return ans
            ans += v
        return -1
        