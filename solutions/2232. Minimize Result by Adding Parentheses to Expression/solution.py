# Problem: Minimize Result by Adding Parentheses to Expression
# Language: python3
# Runtime: 81 ms
# Memory: 14 MB

class Solution:
    def minimizeResult(self, E: str) -> str:
        ind = E.find("+")
        ans = E
        me = eval(ans)
        for l in range(ind-1,-1,-1):
            for r in range(ind+1,len(E)):
                
                if l > 0:
                    ex = E[:l] + "*(" + E[l:r+1]
                    #print(E[:l] + "*(" + E[l:r+1] + ")" + E[r+1:])
                else:
                    ex = E[:l] + "(" + E[l:r+1]
                    #print(E[:l] + "(" + E[l:r+1] + ")" + E[r+1:])
                if r < len(E) - 1:
                    ex += ")*" + E[r+1:]
                else:
                    ex += ")" + E[r+1:]
                m2 = eval(ex)
                if m2 <= me:
                    me = m2
                    ans = ex
        return ans.replace("*","")