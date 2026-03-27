# Problem: Group the People Given the Group Size They Belong To
# Language: python3
# Runtime: 61 ms
# Memory: 16.5 MB

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        g = defaultdict(list)
        
        for i,s in enumerate(groupSizes):
            g[s].append(i)

        ans = []
        for s in g:
            for j in range(0, len(g[s]), s):
                ans.append(g[s][j:j+s])
        
        return ans