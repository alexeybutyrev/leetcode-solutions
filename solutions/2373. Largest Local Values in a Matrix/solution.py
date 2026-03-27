# Problem: Largest Local Values in a Matrix
# Language: python3
# Runtime: 321 ms
# Memory: 14.3 MB

class Solution:
    def largestLocal(self, A: List[List[int]]) -> List[List[int]]:
        N = len(A)
        ans = []
        
        for i in range(1,N-1):
            r = []
            for j in range(1,N-1):
                c = -1
                for l1 in range(i-1,i+2):
                    for l2 in range(j-1,j+2):
                        c = max(c,A[l1][l2])
                r.append(c)
            ans.append(r)
        return ans