# Problem: Lexicographically Minimum String After Removing Stars
# Language: python3
# Runtime: 589 ms
# Memory: 22.1 MB

class Solution:
    def clearStars(self, s: str) -> str:
        stack = []
        c = Counter()
        loc = defaultdict(list)
        
        ans = list(s)
        for i,x in enumerate(s):
            if x == "*":
                k = min(list(loc.keys()))
                j = loc[k][-1]
                #while len(loc[k]) > 0 and loc[k][-1] == j:
                ans[loc[k].pop()] = ''
                #    j-= 1
                if not loc[k]:
                    del loc[k]
                ans[i] = ''
            else:
                loc[x].append(i)
                
        ans = ''.join(ans)
        return ans.replace('*','')