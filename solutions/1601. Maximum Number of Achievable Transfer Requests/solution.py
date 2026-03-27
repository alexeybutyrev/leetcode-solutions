# Problem: Maximum Number of Achievable Transfer Requests
# Language: python3
# Runtime: 1975 ms
# Memory: 58.4 MB

class Solution:
    def maximumRequests(self, n: int, A: List[List[int]]) -> int:
        
        mask = 0
        N = len(A)
        ans = 0
        c = [0]*n
        @cache
        def dp(c,count,i):
            if i == N:
                if all([x==0 for x in c]):
                    return count
                else:
                    return 0
            else:
                
                ans = dp(c,count,i+1)
                c = list(c)
                c[A[i][0]]+=1
                c[A[i][1]]-=1
                return max(dp(tuple(c),count+1,i+1),ans)
        return dp(tuple(c),0,0)
        