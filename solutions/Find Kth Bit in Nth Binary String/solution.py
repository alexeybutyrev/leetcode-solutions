# Problem: Find Kth Bit in Nth Binary String
# Language: python3
# Runtime: 331 ms
# Memory: 30.8 MB

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(c):
            d = {'0':'1','1':'0'}
            res = [d[l] for l in c]
            return "".join(reversed(res))
                
        
        s = "0"
        for _ in range(n-1):
            s += "1" + helper(s)
        
        return s[k-1]