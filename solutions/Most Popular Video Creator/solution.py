# Problem: Most Popular Video Creator
# Language: python3
# Runtime: 870 ms
# Memory: 63.2 MB

class Solution:
    def mostPopularCreator(self, C: List[str], I: List[str], V: List[int]) -> List[List[str]]:
        count = Counter()
        mx = Counter()
        ids = {}
        for c, v,i in zip(C,V,I):
            count[c] += v
            if c not in ids:
                mx[c] = v
                ids[c] = i
            else:
                if v > mx[c]:
                    ids[c] = i
                    mx[c] = v
                elif v == mx[c]:
                    ids[c] = min(i,ids[c])
        
        ans = 0
        for k,v in count.items():
            ans = max(ans,v)
        
        creators = []
        for k,v in count.items():
            if v == ans:
                creators.append([k,ids[k]])
        return creators
        
        