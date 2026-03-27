# Problem: Minimum Operations to Transform Array
# Language: python3
# Runtime: 66 ms
# Memory: 31.2 MB

class Solution:
    def minOperations(self, A: List[int], B: List[int]) -> int:
        x = B.pop()

        ans = 0
        lans = 0
        for a,b in zip(A,B):
            if a <= x <= b or b <= x <= a:
                lans = 1
            ans += abs(b-a)
        if lans: return ans + lans

        lans = inf
        for y in A:
            lans = min( abs(y - x) + 1, lans)
        for y in B:
            lans = min(abs(y - x) + 1, lans)
        return lans + ans
            