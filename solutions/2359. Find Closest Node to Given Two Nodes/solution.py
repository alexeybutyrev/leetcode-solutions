# Problem: Find Closest Node to Given Two Nodes
# Language: python3
# Runtime: 1432 ms
# Memory: 29 MB

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        d1 = [-1] * (N:=len(edges))
        
        node = node1
        c = 0
        while node != -1:
            if d1[node] != -1:
                break
            d1[node] = c
            c += 1
            node = edges[node]
        
        node = node2
        d2 = [-1] * (N:=len(edges))
        c = 0
        while node != -1:
            if d2[node] != -1:
                break
            d2[node] = c
            c += 1
            node = edges[node]
        
        
        d = inf
        ans = -1
        for i,(a,b) in enumerate(zip(d1,d2)):
            if a >= 0 and b >= 0 and d > max(a,b):
                ans = i
                d = max(a,b)
        return ans