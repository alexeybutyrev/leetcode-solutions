# Problem: Freedom Trail
# Language: python3
# Runtime: 1010 ms
# Memory: 21.2 MB

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        letters = set(ring)
        N = len(ring)
        left      = defaultdict(dict)
        left_dist = defaultdict(dict)
        for i in range(N):
            for l in letters:
                for j in range(1,N+1):
                    ind = i - j
                    if ind < 0:
                        ind += N
                    if ring[ind] == l:
                        break
                left[i][l] = ind
                left_dist[i][l] = j
        
        
        right      = defaultdict(dict)
        right_dist = defaultdict(dict)
        reversed_ring = ring
        for i in range(N):
            for l in letters:
                for j in range(1,N+1):
                    ind = i + j
                    if ind >= N:
                        ind -= N
                    if ring[ind] == l:
                        break
                right[i][l] = ind
                right_dist[i][l] = j
        
        M = len(key)
        @cache
        def dp(i,j):
            if j == M:
                return 0
            
            s1 = inf
            if ring[i] == key[j]:
                s1 = 1 + dp(i,j+1)
            
            s2 = left_dist[i][key[j]] + 1 + dp(left[i][key[j]],j+1)
            
            s3 = right_dist[i][key[j]] + 1 + dp(right[i][key[j]],j+1)
            
            return min(s1,s2,s3)
                
            
        return dp(0,0)
        
        
            
        
                        