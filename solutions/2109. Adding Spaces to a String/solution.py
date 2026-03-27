# Problem: Adding Spaces to a String
# Language: python3
# Runtime: 949 ms
# Memory: 51.6 MB

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j = 0
        ans = ""
        for i,l in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                ans += " "
                j+=1
            ans += l
        return ans