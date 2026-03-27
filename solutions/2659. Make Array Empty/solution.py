# Problem: Make Array Empty
# Language: python3
# Runtime: 738 ms
# Memory: 35.3 MB

class Solution:
    def countOperationsToEmptyArray(self, A: List[int]) -> int:
        hm = {x : i+1 for i,x in enumerate(A)}
        N = len(A)
        ans = 0
        i = 0
        for j,x in enumerate(sorted(A)):
            if hm[x] < i:
                ans += N - j
            i = hm[x]
        return ans + N