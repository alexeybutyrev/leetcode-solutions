# Problem: The Employee That Worked on the Longest Task
# Language: python3
# Runtime: 856 ms
# Memory: 14.1 MB

class Solution:
    def hardestWorker(self, n: int, A: List[List[int]]) -> int:
        A = [(-1,0)] + A
        
        ans = 0
        d = -1
        B = []
        for i in range(1,len(A)):
            B.append((A[i][1] - A[i-1][1], A[i][0]))
        
        B.sort(key = lambda x: (-x[0],x[1]))
        return B[0][1]
                