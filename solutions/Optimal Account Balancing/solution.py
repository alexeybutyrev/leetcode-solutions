# Problem: Optimal Account Balancing
# Language: python3
# Runtime: 4056 ms
# Memory: 79.9 MB

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        hm = {}
        ind = 0
        for x,y,z in transactions:
            if x not in hm:
                hm[x] = ind
                ind += 1
            if y not in hm:
                hm[y] = ind
                ind += 1
        
        N = len(hm)
        
        A = [0] * N
        
        for x,y,c in transactions:
            A[hm[x]] -= c
            A[hm[y]] += c
        
        A = [x for x in A if x]
        
        @cache
        def dp(A):
            if not A: return 0
            B = []
            ans = inf
            A = list(A)
            for i in range(len(A)):
                if A[i] > 0:
                    for j in range(len(A)):
                        if A[j] < 0:
                            if A[i] == -A[j]:
                                if i < j:
                                    B = A[:i] + A[i+1:j] + A[j+1:]
                                else:
                                    B = A[:j] + A[j+1:i] + A[i+1:]
                            elif A[i] < -A[j]:
                                B = A[:]
                                B[j] += A[i]
                                B = B[:i] + B[i+1:]
                            else:
                                B = A[:]
                                B[i] += A[j]
                                B = B[:j] + B[j+1:]
                                
                            
                            ans = min(ans, 1 + dp(tuple(B)))
            return ans
        return dp(tuple(A))