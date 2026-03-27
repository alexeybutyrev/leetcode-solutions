# Problem: Find And Replace in String
# Language: python3
# Runtime: 36 ms
# Memory: 14.2 MB

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        R = []
        for i, s, t  in zip(indexes, sources, targets):
            ind = S.find(s,i)
            if ind == i:
                R.append((i,t,s))
        
        R.sort()
        S = list(S)
        j = 0
        ans = []
        t = ""
        i =0
        while i < len(S):
            if j < len(R) and R[j][0] == i:
                ans.append(t)
                ans.append(R[j][1])
                
                i += len(R[j][2])
                j+=1
                t = ""
            else:
                t += S[i]
                i += 1
        ans.append(t)
        return "".join(ans)