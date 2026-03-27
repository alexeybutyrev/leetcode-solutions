# Problem: Mice and Cheese
# Language: python3
# Runtime: 976 ms
# Memory: 32.8 MB

class Solution:
    def miceAndCheese(self, A1: List[int], A2: List[int], k: int) -> int:
        
        A = [(x,y) for x,y in zip(A1,A2)]
        A.sort(key = lambda x: -x[0] + x[1])

        N = len(A)
        s = 0
        for i in range(k):
            s += A[i][0]

        for i in range(k,N):

            s += A[i][1]
        return s
            