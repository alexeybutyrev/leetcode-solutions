# Problem: Special Permutations
# Language: python3
# Runtime: 3223 ms
# Memory: 219.6 MB

class Solution:
    def specialPerm(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        
        graph = defaultdict(list)
        N = len(A)
        for i in range(N):
            for j in range(i+1,N):
                if (A[i] % A[j] == 0) or (A[j]%A[i] == 0):
                    graph[i].append(j)
                    graph[j].append(i)
        
        T = (1<<N) - 1
        @cache
        def dp(i,mask):
            if T == mask:
                return 1
            ans = 0
            for j in graph[i]:
                if (mask & (1<<j)) == 0:
                    ans += dp(j, mask | (1<<j))
                    ans %= MOD
            return ans % MOD
        
        return sum(dp(i,1<<i) for i in range(N)) % MOD
