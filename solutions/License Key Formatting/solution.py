# Problem: License Key Formatting
# Language: python3
# Runtime: 56 ms
# Memory: 14.5 MB

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        ans = ""
        N = len(S)
        count = 0
        for i,l in enumerate(reversed(S)):
            if l != '-':
                ans += l.upper()
                count += 1
                if count == K:
                    count = 0
                    ans += '-'
        
        return ans[::-1].lstrip('-')

            
        