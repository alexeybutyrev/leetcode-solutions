# Problem: Number of Subarrays With AND Value of K
# Language: python3
# Runtime: 1577 ms
# Memory: 27.4 MB

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        c = Counter()
        ans = 0
        for x in nums:
            c1 = Counter()
            if x & k == k:
                c[x] += 1
                for ky,v in c.items():
                    c1[ky & x ] += v
                ans += c1[k]
                
            c = c1
        return ans