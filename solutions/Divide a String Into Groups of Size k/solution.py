# Problem: Divide a String Into Groups of Size k
# Language: python3
# Runtime: 54 ms
# Memory: 14.4 MB

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        N = len(s)
        if N % k !=0:
            s += (k - N % k) * fill

        ans = []
        for i in range(len(s) // k):
            ans.append(s[i*k:(i+1)*k])
        return ans