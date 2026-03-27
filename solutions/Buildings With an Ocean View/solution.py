# Problem: Buildings With an Ocean View
# Language: python3
# Runtime: 600 ms
# Memory: 34.3 MB

from sortedcontainers import SortedList
class Solution:
    def findBuildings(self, H: List[int]) -> List[int]:
            
        ans = []
        for i,x in enumerate(H):
            while ans and H[ans[-1]] <= x:
                ans.pop()
            ans.append(i)
        return ans