# Problem: Reverse Letters Then Special Characters in a String
# Language: python3
# Runtime: 4 ms
# Memory: 19.2 MB

class Solution:
    def reverseByType(self, s: str) -> str:
        L = []
        S = []
        for x in s:
            if x.isalpha():
                L.append(x)
            else:
                S.append(x)
        ans = []
        for x in s:
            if x.isalpha():
                ans.append(L.pop())
            else:
                ans.append(S.pop())
        return "".join(ans)
        