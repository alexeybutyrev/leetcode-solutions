# Problem: Can You Eat Your Favorite Candy on Your Favorite Day?
# Language: python3
# Runtime: 2320 ms
# Memory: 72.9 MB

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        ca = [(0, candiesCount[0])]
        for iC in range(1,len(candiesCount)):
            ca.append((ca[-1][1]+1,ca[-1][1]+candiesCount[iC]))

        res = []
        for t, d, c in queries:
            if (d + 1 <= ca[t][1] and
                ca[t][0] <= (d + 1)*c
               ):
                res.append(True)
                
            else:
                res.append(False)
            
                
                    
        return res