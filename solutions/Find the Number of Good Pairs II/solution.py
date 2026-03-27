# Problem: Find the Number of Good Pairs II
# Language: python3
# Runtime: 1178 ms
# Memory: 42.6 MB

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], V: int) -> int:
        c = Counter(nums1)
        mx = max(nums1)
        @cache
        def solve(x):
            d = x * V
            curr = d
            ans = 0
            while curr <= mx:
                if curr in c:
                    ans += c[curr]
                curr += d
            return ans
        
        ans = 0
        for x in nums2:
            ans += solve(x)
        
        return ans