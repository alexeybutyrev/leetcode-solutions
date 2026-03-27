# Problem: Minimum Time to Remove All Cars Containing Illegal Goods
# Language: python3
# Runtime: 2523 ms
# Memory: 19.5 MB

class Solution:
    def minimumTime(self, s: str) -> int:
        N = len(s)
        def kadein(nums):
            curr = ans = nums[0]
            for a in nums[1:]:
                curr = max(a, curr + a)
                ans = max(ans, curr)
            return ans
        
        A = [-1 if l == '1' else 1 for l in s]
        return N - max(0,kadein(A))