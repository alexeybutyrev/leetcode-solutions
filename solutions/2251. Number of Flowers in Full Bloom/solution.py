# Problem: Number of Flowers in Full Bloom
# Language: python3
# Runtime: 1013 ms
# Memory: 42.8 MB

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        A = []
        for s,e in flowers:
            A.append([s,1])
            A.append([e+1,-1])
        A.sort()
        
        N = len(A)
        for i in range(1,N):
            A[i][1] += A[i-1][1]
        
        I = [x for x,y in A]
        ans = []
        for p in people:
            ind = bisect_right(I,p)-1
            ans.append(A[ind][-1])
        return ans