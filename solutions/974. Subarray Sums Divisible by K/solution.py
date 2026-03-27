# Problem: Subarray Sums Divisible by K
# Language: python3
# Runtime: 250 ms
# Memory: 21.4 MB

class Solution:
    def subarraysDivByK(self, A: List[int], k: int) -> int:
        c = Counter()
        c[0] = 1
        
        s = 0
        ans = 0
        for a in A:
            s += a
            m = s % k
            ans += c[m]
            c[m] += 1
        return ans
        