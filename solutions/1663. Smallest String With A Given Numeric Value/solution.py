# Problem: Smallest String With A Given Numeric Value
# Language: python3
# Runtime: 692 ms
# Memory: 15.8 MB

class Solution:
    def getSmallestString(self, n: int, S: int) -> str:
        
        ans = ""
        for i in range(n-1,-1,-1):
            if S <= i * 26:
                S -= 1
                ans += 'a'
            else:
                c = S - 26 * i
                ans += chr(ord('a') + c-1)
                S -= c
        
        return ans
            
            