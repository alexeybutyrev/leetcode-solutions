# Problem: Minimum Number of Operations to Move All Balls to Each Box
# Language: python3
# Runtime: 5996 ms
# Memory: 14.5 MB

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        A = list(map(int, list(boxes)))
        N = len(A)
        res = [0] * N
        
        for i in range(N):
            for j in range(N):
                if A[j]:
                    res[i] += abs(j-i)
        
        return res