# Problem: Rotate String
# Language: python3
# Runtime: 0 ms
# Memory: 16.4 MB

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            #print(s[:i] + s[i:], goal)
            if s[i:] + s[:i] == goal:
                return True
        return False