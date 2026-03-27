# Problem: First Unique Even Element
# Language: python3
# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def firstUniqueEven(self, A: list[int]) -> int:
        c = Counter(A)

        for x in A:
            if x%2 == 0 and c[x] == 1:
                return x
        return -1