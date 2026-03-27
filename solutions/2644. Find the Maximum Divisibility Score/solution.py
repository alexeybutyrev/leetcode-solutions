# Problem: Find the Maximum Divisibility Score
# Language: python3
# Runtime: 5170 ms
# Memory: 14.1 MB

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        c = Counter()
        s = set(divisors)
        for x in nums:
            for d in s:
                if x % d == 0:
                    c[d] += 1
        
        S = list(sorted(s))
        mx = c[S[0]]
        
        ans = S[0]
        for x in S[1:]:
            if c[x] > mx:
                ans = x
                mx = c[x]
        return ans
                