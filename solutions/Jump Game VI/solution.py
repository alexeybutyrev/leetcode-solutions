# Problem: Jump Game VI
# Language: python3
# Runtime: 1188 ms
# Memory: 27.5 MB

class Solution:
    def maxResult(self, A: List[int], k: int) -> int:
        N = len(A)
        score = [0] * N
        score[0] = A[0]
        q = deque([0])
        
        for i in range(1,N):
            while q and q[0] + k < i:
                q.popleft()
            
            score[i] = score[q[0]] + A[i]
            while q and score[i] >= score[q[-1]]:
                q.pop()
            q.append(i)
        
        return score[-1]