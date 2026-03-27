# Problem: Find the Number of Distinct Colors Among the Balls
# Language: python3
# Runtime: 1207 ms
# Memory: 68.4 MB

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        c = {}
        cols = Counter()
        ans = []
        for x,y in queries:
            if x in c:
                cols[c[x]] -= 1
                if not cols[c[x]]:
                    del cols[c[x]]
            cols[y] += 1
            c[x] = y
            ans.append(len(cols))
        return ans