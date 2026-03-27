# Problem: Minimum Operations to Make All Array Elements Equal
# Language: python3
# Runtime: 1210 ms
# Memory: 46.5 MB

class Solution:
    def minOperations(self, A: List[int], queries: List[int]) -> List[int]:
        A.sort()
        N = len(A)

        L = [0]
        for i in range(1,N):
            L.append(L[-1]  + (A[i] - A[i-1]) * i)

        R = [0]
        for i in range(N-2,-1,-1):
            delta = (A[i+1] - A[i])
            R.append(R[-1] + delta * (N -1 - i) )

        R = R[::-1]

        ans = []
        for x in queries:

            ind = bisect_right(A,x)
            
            if ind == N:
                d = x - A[-1]
                ans.append(L[-1] + d * N)
                continue
            else:
                print(ind)
                
                d = A[ind] - x
                sl = L[ind] - d * (ind)
                sr = R[ind] + d * (N - ind)

                ans.append(sl + sr)
        return ans
            
        
        
        