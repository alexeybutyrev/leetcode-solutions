# Problem: Find Minimum Time to Finish All Jobs
# Language: python3
# Runtime: 212 ms
# Memory: 14.3 MB

class Solution:
    def minimumTimeRequired(self, A: List[int], k: int) -> int:
        N = len(A)
        L = [0] * k
        ans = inf
        A.sort()
        
        def dfs(i):
            nonlocal ans
            if i == N:
                ans = min(ans, max(L))
            else:
                #used = set()
                for j in range(k):
                    #if L[j] in used: continue
                    if L[j] + A[i] >= ans: continue
                    
                    #used.add(L[j])
                    
                    L[j] += A[i]
                    dfs(i+1)
                    L[j] -= A[i]
                    
                    if L[j] == 0:
                        break
        
        dfs(0)
        return ans 
        