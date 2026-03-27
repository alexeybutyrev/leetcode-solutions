# Problem: Naming a Company
# Language: python3
# Runtime: 831 ms
# Memory: 28.5 MB

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        s = defaultdict(set)
        for w in ideas:
            s[w[0]].add(w[1:])
        ans = 0
        for x,y in combinations(s.keys(),2):
            c1 = len(s[x] - (s[x] & s[y]))
            c2 = len(s[y] - (s[x] & s[y]))
            
            ans += 2 * c1 * c2
        return ans
            