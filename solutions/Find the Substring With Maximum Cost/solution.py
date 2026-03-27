# Problem: Find the Substring With Maximum Cost
# Language: python3
# Runtime: 324 ms
# Memory: 16.4 MB

from string import ascii_lowercase
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        hm = {l: i + 1for i,l in enumerate(ascii_lowercase)}
        for c,v in zip(chars,vals):
            hm[c] = v
        
        A = [0]
        for l in s:
            A.append(hm[l])

        curr = ans = A[0]
        
        for a in A[1:]:
            curr = max(a, curr + a)
            ans = max(ans, curr)
        
        return ans
        
            