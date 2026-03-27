# Problem: Count Subarrays With Fixed Bounds
# Language: python3
# Runtime: 2101 ms
# Memory: 29 MB


class Solution:
    def countSubarrays(self, A: List[int], MIN: int, MAX: int) -> int:
        N = len(A)
        l = r = -1
        ans = j = 0
        for i,a in enumerate(A):
            if not (MIN <= a <= MAX):
                l,r,j = -1,-1,i+1
            if a == MIN: l = i
            if a == MAX: r = i
            ans +=  max(0, min(l,r) - j + 1)
        return ans