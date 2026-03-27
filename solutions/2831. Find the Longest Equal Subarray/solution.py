# Problem: Find the Longest Equal Subarray
# Language: python3
# Runtime: 1463 ms
# Memory: 36.5 MB

class Solution:
    def longestEqualSubarray(self, A: List[int], k: int) -> int:
        N = len(A)
        D = defaultdict(list)
        for i,x in enumerate(A):
            D[x].append(i)
        
        def solve(A,K):
            k = K
            N = len(A)
            
            i = 0
            j = 1
            ans = 1
            
            while i < N and j <N:
                d = A[j] - A[j-1] - 1
                k -= d
                if k < 0:
                    while i < j and k < 0:
                        k += A[i+1] - A[i] - 1
                        i += 1
                    
                ans = max(ans, j - i + 1)

                j+=1
                
            return ans
                    
                
            
        
        ans = 0
        for x in D:
            s = solve(D[x],k)
            ans = max(ans, s)
        
        return ans