# Problem: Reduction Operations to Make the Array Elements Equal
# Language: python3
# Runtime: 878 ms
# Memory: 27 MB

class Solution:
    def reductionOperations(self, A: List[int]) -> int:
        s = list(sorted(set(A)))
        ans=0
        for x in sorted(A, reverse=True):
            if x !=s[-1]:
                s.pop()
            ans += len(s)-1
        return ans
            