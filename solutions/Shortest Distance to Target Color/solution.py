# Problem: Shortest Distance to Target Color
# Language: python3
# Runtime: 1656 ms
# Memory: 37.2 MB

class Solution:
    def shortestDistanceColor(self, A: List[int], queries: List[List[int]]) -> List[int]:
        hm = defaultdict(list)
        
        for i,c in enumerate(A):
            hm[c].append(i)
        
        ans = []
        
        for i, c in queries:
            if c not in hm:
                ans.append(-1)
            else:
                ind = bisect.bisect(hm[c],i)
                if ind == 0:
                    ans.append(hm[c][0] - i)
                elif ind == len(hm[c]):
                    ans.append(i - hm[c][-1])
                else:
                    ans.append(min(i - hm[c][ind-1], hm[c][ind] - i))
                    
        return ans