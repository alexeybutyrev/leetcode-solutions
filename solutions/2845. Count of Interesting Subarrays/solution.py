# Problem: Count of Interesting Subarrays
# Language: python3
# Runtime: 863 ms
# Memory: 34.5 MB

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        c = Counter()
        ans = 0
        c[0] = 1
        ps = 0
        for x in nums:
            if x % modulo == k:
                ps += 1
            ps %= modulo
            ans += c[(ps - k) % modulo]
            c[ps] += 1
        return ans