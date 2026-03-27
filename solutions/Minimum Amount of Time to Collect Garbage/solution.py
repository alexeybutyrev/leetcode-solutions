# Problem: Minimum Amount of Time to Collect Garbage
# Language: python3
# Runtime: 778 ms
# Memory: 39.5 MB

class Solution:
    def garbageCollection(self, G: List[str], T: List[int]) -> int:
        m,p,g = 0,0,0
        t = 0
        T = list(accumulate(T,initial=0))
        last = Counter()
        ans = 0
        for i in range(len(G)):
            if "M" in G[i]:
                m = T[i]
            if "G" in G[i]:
                g = T[i]
            if "P" in G[i]:
                p = T[i]
            ans+=len(G[i])
        return ans + p + g + m
            