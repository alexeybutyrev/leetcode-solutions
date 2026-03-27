# Problem: Find the Score of All Prefixes of an Array
# Language: python3
# Runtime: 560 ms
# Memory: 34.2 MB

class Solution:
    def findPrefixScore(self, A: List[int]) -> List[int]:
        x = 0
        ans = []
        for a in A:
            x = max(a,x)
            ans.append(a + x)
        return accumulate(ans)