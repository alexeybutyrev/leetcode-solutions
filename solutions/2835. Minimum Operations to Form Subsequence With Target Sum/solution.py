# Problem: Minimum Operations to Form Subsequence With Target Sum
# Language: python3
# Runtime: 65 ms
# Memory: 16.6 MB

class Solution:
    def minOperations(self, A: List[int], t: int) -> int:
        A.sort()
        s = sum(A)
        if s < t: return -1
        ans = 0
        while t:
            a = A.pop()
            if s-a >= t:
                s -= a
            elif a <= t:
                t -= a
                s -= a
            else:
                A.append( a//2)
                A.append( a//2)
                ans += 1
        return ans
                