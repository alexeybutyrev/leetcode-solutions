# Problem: Find All Possible Recipes from Given Supplies
# Language: python3
# Runtime: 848 ms
# Memory: 16.9 MB

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        counts = list(map(len, ingredients))
        
        r = defaultdict(list)
        for i,ing in enumerate(ingredients):
            for v in ing:
                r[v].append(i)
                
        
        q = supplies
        ans = []
        for ing in q:
            for i in r[ing]:
                counts[i] -= 1
                if not counts[i]:
                    q.append(recipes[i])
                    ans.append(recipes[i])
        return ans
        
                