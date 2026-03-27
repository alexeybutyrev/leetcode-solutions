# Problem: Isomorphic Strings
# Language: python3
# Runtime: 38 ms
# Memory: 16.7 MB

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        X={}
        Y={}
        for x,y in zip(s,t):
            if x in X and y in Y and X[x]==y and Y[y]==y: continue
            if x not in X and y not in Y:
                X[x]=y
                Y[y]=y
                continue
            return False
        return True