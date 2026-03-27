# Problem: Largest Number After Digit Swaps by Parity
# Language: python3
# Runtime: 24 ms
# Memory: 14 MB

class Solution:
    def largestInteger(self, num: int) -> int:
        n = str(num)
        ans = n
        odd = []
        even = []
        for i,l in enumerate(n):
            if int(l) & 1:
                odd.append((l,i))
            else:
                even.append((l,i))
        
        odd.sort()
        even.sort()
        
        ans = ""
        for i,l in enumerate(n):
            if int(l) & 1:
                ans += odd.pop()[0]
            else:
                ans += even.pop()[0]
        
        return int(ans)
        
        
        
                