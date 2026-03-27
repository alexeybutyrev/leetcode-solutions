# Problem: Sum of Even Numbers After Queries
# Language: python3
# Runtime: 548 ms
# Memory: 20.9 MB

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        s = 0
        inds = set()
        for i,x in enumerate(A):
            if x % 2 == 0:
                s += x
                inds.add(i)
        
        ans = []
        for v,i in queries:
            if i in inds:
                s -= A[i]
                if (A[i] + v) % 2 == 0:
                    A[i] += v
                    s += A[i]
                else:
                    A[i] += v
                    inds.remove(i)
            else:
                A[i] += v
                if A[i] % 2 == 0:
                    inds.add(i)
                    s += A[i]
                
            ans.append(s)
        return ans
                    