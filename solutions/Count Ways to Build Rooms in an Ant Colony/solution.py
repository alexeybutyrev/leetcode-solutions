# Problem: Count Ways to Build Rooms in an Ant Colony
# Language: python3
# Runtime: 5092 ms
# Memory: 225.9 MB

class Solution:
    def waysToBuildRooms(self, A: List[int]) -> int:
        N = len(A)
        MOD = 10 ** 9 + 7
        children = defaultdict(set)
        for i in range(1,N):
            children[A[i]].add(i)
        
        @cache
        def dfs(node):
            if not children[node]:
                return 1, 1
            ans, l = 1, 0
            for n in children[node]:
                tmp, r = dfs(n)
                ans = (ans * tmp * math.comb(l+r, r)) % MOD
                l += r
            return ans, l + 1
            
        return dfs(0)[0]
    