# Problem: Reverse String II
# Language: python3
# Runtime: 39 ms
# Memory: 16.5 MB

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        L =list(s)
        for i in range(0,len(L),2*k):
            L[i:i+k] = L[i:i+k][::-1]
        return "".join(L)