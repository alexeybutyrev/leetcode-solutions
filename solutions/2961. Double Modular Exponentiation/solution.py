# Problem: Double Modular Exponentiation
# Language: python3
# Runtime: 57 ms
# Memory: 16.4 MB

class Solution:
    def getGoodIndices(self, variables: List[List[int]], T: int) -> List[int]:
        ans = []
        for i,(a, b, c, m) in enumerate(variables):
            if pow(pow(a,b,10), c, m) == T:
                ans.append(i)
        return ans
        