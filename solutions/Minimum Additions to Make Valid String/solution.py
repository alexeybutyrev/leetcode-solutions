# Problem: Minimum Additions to Make Valid String
# Language: python3
# Runtime: 54 ms
# Memory: 14 MB

class Solution:
    def addMinimum(self, word: str) -> int:
        s = []
        ans = 0
        for l in word:
            
            if l == 'a':
                if not s:
                    s.append('a')
                else:
                    if len(s) == 2:
                        ans += 1
                    else:
                        ans += 2
                    s = ['a']
            elif l == 'b':
                if not s:
                    ans += 1
                    s = ['a','b']
                else:
                    if s[-1] == 'b':
                        ans += 2
                    s = ['a','b']
            else:
                if not s:
                    ans += 2
                else:
                    if len(s) == 1:
                        ans += 1
                    s = []
            print(l,s, ans)
        x = 0
        if len(s) == 1:
            x = 2
        if len(s) == 2:
            x = 1
        return ans + x