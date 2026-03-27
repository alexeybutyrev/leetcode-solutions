# Problem: Count Zero Request Servers
# Language: python3
# Runtime: 1718 ms
# Memory: 80.2 MB

class Solution:
    def countServers(self, n: int, A: List[List[int]], x: int, queries: List[int]) -> List[int]:
        A.sort(key = lambda x: x[1])
        ans = [0] * len(queries)
        N = len(A)
        s = e = 0
        used = 0
        c = Counter()
        
        for (t,i) in sorted((t,i) for i,t in enumerate(queries)):
            
            while s < N and A[s][1] <= t:
                c[A[s][0]] += 1
                used += (c[A[s][0]] == 1)
                s += 1
            
            while e < s and A[e][1] < t - x:
                c[A[e][0]] -= 1
                used -= (c[A[e][0]] == 0)
                e += 1
            
            ans[i] = n - used
        return ans