# Problem: Four Divisors
# Language: python3
# Runtime: 102 ms
# Memory: 18.7 MB


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        @cache
        def dev(x):
            seen = set()
            for a in range(1,floor(sqrt(x)) +1 ):
                if x % a == 0:
                    seen.add(x//a)
                    seen.add(a)
                    if len(seen) > 4:
                        return 0
            if len(seen) == 4:
                return sum(seen)
            return 0
        
        ans = 0
        for x in nums:
            s = dev(x)
            ans += s
        return ans