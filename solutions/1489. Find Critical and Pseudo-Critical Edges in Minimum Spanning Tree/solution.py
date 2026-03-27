# Problem: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
# Language: python3
# Runtime: 125 ms
# Memory: 16.5 MB

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges=[x+[i] for i,x in enumerate(edges)]
        ce,pce=set(),set()
        while any([e[0]!=e[1] for e in edges]):
            temp=min([e[2] for e in edges])
            s=[e for e in edges if e[2]==temp]
            for i in range(len(s)):
                temp2=[x[:] for x in s]
                for j in range(len(s)):
                    if i!=j:
                        f,t,w,id=temp2[j]
                        for e in temp2:
                            if e[0]==t:
                                e[0]=f
                            if e[1]==t:
                                e[1]=f
                if temp2[i][0]==temp2[i][1]:
                    pce.add(temp2[i][3])
                else:
                    ce.add(temp2[i][3])
            for f,t,w,i in s:
                for e in edges:
                    if e[0]==t:
                        e[0]=f
                    if e[1]==t:
                        e[1]=f
            edges=[e for e in edges if e[2]!=temp and e[0]!=e[1]]
        return [list(ce),list(pce)]