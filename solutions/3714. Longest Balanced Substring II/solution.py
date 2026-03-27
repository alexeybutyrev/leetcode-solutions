# Problem: Longest Balanced Substring II
# Language: python3
# Runtime: 2294 ms
# Memory: 134.3 MB

class Solution:
    def longestBalanced(self, S: str) -> int:
        N = len(S)
        P = [[0,0,0]]

        d = {}
        for x in S:
            P.append(P[-1][:])
            P[-1]["abc".index(x)] += 1
        
        ans = 0
        for i, (a,b,c) in enumerate(P):
            for key in [
                ("abc",a-b,a-c),
                ("ab",a-b,c),
                ("ca",c-a,b),
                ("bc",b-c,a),
                ("a",b,c),
                ("b",c,a),
                ("c",a,b),
            ]:
                ans = max(ans, i - d.get(key,i))
                d.setdefault(key,i)
        return ans