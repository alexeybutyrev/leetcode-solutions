# Problem: Most Beautiful Item for Each Query
# Language: python3
# Runtime: 174 ms
# Memory: 63.9 MB

class Solution:
    def maximumBeauty(self, A: List[List[int]], queries: List[int]) -> List[int]:
        A.sort(key = lambda x: (x[0], -x[1]))
        
        I = [A[0][0]]
        for i in range(1, N:=len(A)):
            A[i][1] = max(A[i][1], A[i-1][1])
            I.append(A[i][0])
        
        ans = []
        for x in queries:
            ind = bisect_right(I,x)-1
            if I[ind] <=x:
                ans.append(A[ind][1])
            else:
                ans.append(0)
        return ans
            