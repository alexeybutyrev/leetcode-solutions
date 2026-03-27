# Problem: String Compression III
# Language: python3
# Runtime: 250 ms
# Memory: 19.7 MB

class Solution:
    def compressedString(self, s: str) -> str:
        ans = ""
        c = 1
        curr = s[0]
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                if c == 9:
                    ans += '9' + curr
                    c = 1
                else:
                    c += 1
            else:
                ans += str(c) + curr
                curr = s[i]
                c = 1
        return ans + str(c) + curr
    
                