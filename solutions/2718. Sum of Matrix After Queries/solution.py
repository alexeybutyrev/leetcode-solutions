# Problem: Sum of Matrix After Queries
# Language: python3
# Runtime: 2729 ms
# Memory: 39.9 MB

from sortedcontainers import SortedList
class Solution:
    def matrixSumQueries(self, N: int, queries: List[List[int]]) -> int:
        cols = {}
        rows = {}
        for time, (t, i, val) in enumerate(queries):
            if t == 0:
                rows[i] = (time,val)
            else:
                cols[i] = (time,val)
        if not cols:
            ans = 0
            for _,v in rows.values():
                ans += N * v
            return ans
        
        A = SortedList()
        for t,v in cols.values():
            A.add([t,v])
        
        I = []
        for i in range(len(A)):
            I.append(A[i][0])
        for i in range(len(A)-2,-1,-1):
            A[i][1] += A[i+1][1]
            
        col_seen = len(A)
        
        ans = 0
        seen = set()
        for i,(t,v) in rows.items():
            seen.add(i)
            ind = bisect_left(I,t)
            if ind == col_seen:
                ans += N * v
            else:
                ans += A[ind][-1] + (ind + N - col_seen) * v

        for i in range(N):
            if i not in seen:
                ans += A[0][-1]
        return ans
            
                