# Problem: Total Waviness of Numbers in Range I
# Language: python3
# Runtime: 275 ms
# Memory: 18 MB

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for x in range(num1,num2+1):
            
            s = str(x)
            
            
            if len(s) >= 3:
                for j in range(2,len(s)):
                    if (s[j-2] < s[j-1] > s[j] or s[j-2] > s[j-1] < s[j]):
                        ans += 1
        return ans