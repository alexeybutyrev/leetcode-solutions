# Problem: XOR Queries of a Subarray
# Language: python3
# Runtime: 300 ms
# Memory: 31.5 MB

class Solution:
    def xorQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        X = [0]
        
        for a in A:
            X.append(X[-1] ^ a)
        
        ans = []
        for l,r in queries:
            ans.append(X[l] ^ X[r+1])
        return ans