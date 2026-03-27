# Problem: Distinct Prime Factors of Product of Array
# Language: python3
# Runtime: 729 ms
# Memory: 15.4 MB

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        x = 1
        s = []
        M = 1
        for a in set(nums):
            s.append(a)
            M = max(a,M)
        ans = set()
        for x in s:
            for i in range(2, 1000):
                if x % i == 0:
                    ans.add(i)
                    while x % i == 0:
                        x //= i
        return len(ans)