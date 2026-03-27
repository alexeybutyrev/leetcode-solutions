# Problem: Find Maximum Balanced XOR Subarray Length
# Language: python3
# Runtime: 525 ms
# Memory: 50.9 MB

class Solution:
    def maxBalancedSubarray(self, A: List[int]) -> int:
        d = {(0,0):-1}

        p = ans = xor = 0
        for i,x in enumerate(A):
            xor ^= x
            p += 1 if x & 1 else -1
            t = (p,xor)
            if t in d:
                ans = max(ans,i - d[t])
            else:
                d[t] = i
        return ans

        