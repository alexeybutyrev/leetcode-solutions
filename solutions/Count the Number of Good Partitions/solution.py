# Problem: Count the Number of Good Partitions
# Language: python3
# Runtime: 1195 ms
# Memory: 59.6 MB

def merge(A: List[List[int]]) -> List[List[int]]:
    A.sort()

    B = [A[0]]
    for x,y in A[1:]:
        if x > B[-1][1]:
            B.append([x,y])
        else:
            B[-1][1] = max(y,B[-1][1])
    return B

class Solution:
    def numberOfGoodPartitions(self, A: List[int]) -> int:
        N = len(A)
        MOD = 10**9 + 7
        
        
        mind = defaultdict(lambda:inf)
        maxd = defaultdict(lambda:-1)
        for i,x in enumerate(A):
            mind[x] = min(mind[x], i)
            maxd[x] = max(maxd[x], i)
        
        A = []
        for x in mind:
            A.append([mind[x], maxd[x]])
        
        A = merge(A)
        
        return pow(2, len(A) - 1, MOD)