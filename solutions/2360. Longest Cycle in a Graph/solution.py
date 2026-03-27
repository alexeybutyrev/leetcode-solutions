# Problem: Longest Cycle in a Graph
# Language: python3
# Runtime: 1766 ms
# Memory: 217.4 MB

class Solution:
    def longestCycle(self, E: List[int]) -> int:
        N = len(E)
#         white  -1
#         grey   0
#         black  1
        
        gseen = set()
        lseen = set()
        D = Counter()
        self.ans = -1
        def walk(i,c):
            nonlocal gseen
            nonlocal lseen
            if E[i] == -1 or i in gseen:
                gseen |= {i} | lseen
            else:
                if i in lseen:
                    gseen |= lseen
                    self.ans = max(self.ans,c - D[i])
                else:
                    lseen.add(i)
                    D[i] = c
                    walk(E[i],c+1)
        
        for i in range(N):
            lseen = set()
            walk(i,0)
                
        return self.ans