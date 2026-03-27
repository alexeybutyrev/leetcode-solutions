# Problem: Number of Equivalent Domino Pairs
# Language: python3
# Runtime: 10 ms
# Memory: 24.2 MB

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = Counter()
        for a,b in dominoes:
            if a > b:
                c[(b,a)] +=1
            else:
                c[(a,b)] +=1
        
        return sum(v * (v - 1) // 2 for _,v in c.items())