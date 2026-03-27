# Problem: Find the Prefix Common Array of Two Arrays
# Language: python3
# Runtime: 155 ms
# Memory: 16.3 MB

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        sA = set()
        sB = set()
        ans = []
        for a,b in zip(A,B):
            sA.add(a)
            sB.add(b)
            ans.append(len(sA&sB))
        return ans