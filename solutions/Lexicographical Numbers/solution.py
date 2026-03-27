# Problem: Lexicographical Numbers
# Language: python3
# Runtime: 70 ms
# Memory: 23.3 MB

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        A = []
        for x in range(1,n+1):
            A.append(str(x))
        A.sort()
        return [int(x) for x in A]