# Problem: Count the Number of Beautiful Subarrays
# Language: python3
# Runtime: 1237 ms
# Memory: 36.1 MB

class Solution:
    def beautifulSubarrays(self, A: List[int]) -> int:
        N = len(A)
        c = Counter()
        s = 0
        c[0] = 1
        ans = 0
        for x in A:
            s ^= x
            ans += c[s]
            c[s] += 1
        return ans