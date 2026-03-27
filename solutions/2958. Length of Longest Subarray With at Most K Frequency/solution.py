# Problem: Length of Longest Subarray With at Most K Frequency
# Language: python3
# Runtime: 1402 ms
# Memory: 31 MB

class Solution:
    def maxSubarrayLength(self, A: List[int], k: int) -> int:
        c = Counter()
        i = 0
        ans = 0
        for j,x in enumerate(A):
            c[x] += 1
            while c[x] > k:
                c[A[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans
            