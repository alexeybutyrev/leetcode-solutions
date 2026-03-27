# Problem: Range Product Queries of Powers
# Language: python3
# Runtime: 5720 ms
# Memory: 51 MB

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        c = bin(n)[2:]
        A = []
        for i,x in enumerate(c[::-1]):
            if x == "1":
                A.append(2 ** i)
        ans = []
        for l,r in queries:
            x = 1
            for i in range(l,r+1):
                x *= A[i]
                x %= MOD
            ans.append(x)
        return ans