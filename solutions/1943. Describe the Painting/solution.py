# Problem: Describe the Painting
# Language: python3
# Runtime: 1304 ms
# Memory: 34.6 MB

class Solution:
    def splitPainting(self, S: List[List[int]]) -> List[List[int]]:
        
        graph = Counter()
        for l,r,c in S:
            graph[l] += c
            graph[r] -= c
        
        A = [(k,v) for k,v in graph.items()]
        A.sort()
        c = A[0][1]
        ans = []
        a = A[0][0]
        for i in range(1,len(A)):
            b = A[i][0]
            if c > 0:
                ans.append([a,b,c])
            
            c += A[i][1]
            a = b
        return ans