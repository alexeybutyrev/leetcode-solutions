# Problem: Shuffle String
# Language: python3
# Runtime: 48 ms
# Memory: 14.1 MB

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        n = len(indices)
        res = [''] * n
        for i in range(n):
            res[indices[i]] = s[i]
        
        
        return "".join(res)