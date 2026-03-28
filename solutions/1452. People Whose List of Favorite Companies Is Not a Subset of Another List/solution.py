# Problem: People Whose List of Favorite Companies Is Not a Subset of Another List
# Language: python3
# Runtime: 660 ms
# Memory: 25.5 MB

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        
        
        res = []
        for i in range(n):
            s1 = set(favoriteCompanies[i])
            flag = True
            for j in range(n):
                if j != i:
                    if len(favoriteCompanies[j]) >= len(favoriteCompanies[i]):
                        
                        if s1.issubset(set(list(favoriteCompanies[j]))):
                            flag = False
                            break
            if flag:
                res.append(i)
        
        return res
        
                