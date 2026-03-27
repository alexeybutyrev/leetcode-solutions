# Problem: Faulty Keyboard
# Language: python3
# Runtime: 42 ms
# Memory: 16.2 MB

class Solution:
    def finalString(self, s: str) -> str:
        ans = ""
        for l in s:
            if l == 'i':
                ans = ans[::-1]
            else:
                ans += l            
        return ans
        