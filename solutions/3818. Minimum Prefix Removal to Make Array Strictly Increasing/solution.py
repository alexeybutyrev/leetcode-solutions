# Problem: Minimum Prefix Removal to Make Array Strictly Increasing
# Language: python3
# Runtime: 12 ms
# Memory: 34.2 MB

class Solution:
    def minimumPrefixLength(self, A: List[int]) -> int:
        N = len(A)
        s = [A.pop()]
        while A:
            if s[-1] > A[-1]:
                s.append(A.pop())
            else:
                break
        return N - len(s)
            
            