# Problem: Partition Array into Disjoint Intervals
# Language: python3
# Runtime: 220 ms
# Memory: 18.2 MB

class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        N = len(A)
        
        R = [inf]
        for j in range(N-2,-1,-1):
            R.append(min(A[j+1], R[-1]))
        R = R[::-1]
        L = [A[0]]
        for i in range(1,N):
            L.append(max(L[-1], A[i]))
        
        for i in range(N):
            if R[i] >= L[i]:
                return i+1
        return N
        