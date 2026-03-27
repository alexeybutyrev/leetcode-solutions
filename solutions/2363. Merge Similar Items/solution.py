# Problem: Merge Similar Items
# Language: python3
# Runtime: 179 ms
# Memory: 14.8 MB

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        c = Counter()
        
        for v,w in items1:
            c[v] +=w
        
        
        for v,w in items2:
            c[v] += w
        
        ans = []
        
        for k,v in c.items():
            ans.append([k, v])
        return sorted(ans)